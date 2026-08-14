import streamlit as st
from retrieval.ingest import ingest_dsa_docs
from graph import app
from tracker import save_score, load_scores, get_stats
from questions import (
    get_random_question, get_all_difficulties,
    get_all_categories, get_random_by_category
)

st.set_page_config(
    page_title="Coding Interview Agent",
    page_icon="💻",
    layout="wide"
)

LANGUAGES = {
    "Python":     {"icon": "🐍", "placeholder": "def solution(...):\n    # write your code here\n    pass"},
    "JavaScript": {"icon": "🟨", "placeholder": "function solution(...) {\n    // write your code here\n}"},
    "TypeScript": {"icon": "🔷", "placeholder": "function solution(...): ReturnType {\n    // write your code here\n}"},
    "Java":       {"icon": "☕", "placeholder": "class Solution {\n    public ReturnType method(...) {\n        // write your code here\n    }\n}"},
    "C++":        {"icon": "⚙️", "placeholder": "class Solution {\npublic:\n    ReturnType method(...) {\n        // write your code here\n    }\n};"},
    "C":          {"icon": "🔩", "placeholder": "// write your solution in C\nreturn_type function_name(...) {\n    // write your code here\n}"},
    "Go":         {"icon": "🐹", "placeholder": "func solution(...) ReturnType {\n    // write your code here\n}"},
    "Rust":       {"icon": "🦀", "placeholder": "fn solution(...) -> ReturnType {\n    // write your code here\n}"},
    "Kotlin":     {"icon": "🟣", "placeholder": "fun solution(...): ReturnType {\n    // write your code here\n}"},
    "Swift":      {"icon": "🍎", "placeholder": "func solution(...) -> ReturnType {\n    // write your code here\n}"},
    "Ruby":       {"icon": "💎", "placeholder": "def solution(...)\n    # write your code here\nend"},
    "PHP":        {"icon": "🐘", "placeholder": "<?php\nfunction solution(...) {\n    // write your code here\n}"},
}

def run_agent(problem: str, user_code: str, intent: str, language: str, hint_level: int = 1):
    initial_state = {
        "problem":           problem,
        "user_code":         user_code,
        "language":          language.lower(),
        "hint_level":        hint_level,
        "retrieved_context": "",
        "hint_output":       None,
        "evaluation_output": None,
        "complexity_output": None,
        "messages":          [],
        "next_agent":        intent,
    }
    result = app.invoke(initial_state)
    if intent == "hint":
        return result["hint_output"]
    elif intent == "evaluator":
        return result["evaluation_output"]
    elif intent == "complexity":
        return result["complexity_output"]

# ── Init ────────────────────────────────────────────────────────
if "db_ready" not in st.session_state:
    with st.spinner("Loading DSA knowledge base..."):
        ingest_dsa_docs()
    st.session_state.db_ready = True

if "current_question" not in st.session_state:
    st.session_state.current_question = get_random_question()

if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Python"

for key in ["hint_result", "eval_result", "complexity_result"]:
    if key not in st.session_state:
        st.session_state[key] = ""

for key in ["show_hint", "show_eval", "show_complexity"]:
    if key not in st.session_state:
        st.session_state[key] = False

def reset_results():
    st.session_state.show_hint       = False
    st.session_state.show_eval       = False
    st.session_state.show_complexity = False
    st.session_state.hint_result       = ""
    st.session_state.eval_result       = ""
    st.session_state.complexity_result = ""

# ── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.title("💻 Interview Agent")
    st.caption("Llama 3.2 + ChromaDB — free & offline")
    st.divider()

    # Stats
    st.subheader("📊 Your Stats")
    stats = get_stats()
    col1, col2 = st.columns(2)
    col1.metric("Attempts",  stats["total"])
    col2.metric("Pass Rate", f"{stats['pass_rate']}%")
    col3, col4 = st.columns(2)
    col3.metric("✅ Passed", stats["passed"])
    col4.metric("❌ Failed", stats["failed"])

    st.divider()

    # Language selector
    st.subheader("🌐 Language")
    lang_names = list(LANGUAGES.keys())
    selected = st.selectbox(
        "Choose your language",
        lang_names,
        format_func=lambda x: f"{LANGUAGES[x]['icon']} {x}",
        index=lang_names.index(st.session_state.selected_language),
        label_visibility="collapsed"
    )
    if selected != st.session_state.selected_language:
        st.session_state.selected_language = selected
        reset_results()
        st.rerun()

    st.divider()

    # Question picker
    st.subheader("🎲 Question Settings")
    difficulty = st.selectbox("Difficulty", get_all_difficulties())
    category   = st.selectbox("Category",   get_all_categories())

    if st.button("🎲 New Random Question", use_container_width=True):
        if category != "Any":
            st.session_state.current_question = get_random_by_category(category)
        else:
            st.session_state.current_question = get_random_question(difficulty)
        reset_results()
        st.rerun()

    st.divider()

    # History
    st.subheader("📜 Recent History")
    scores = load_scores()
    if not scores:
        st.caption("No attempts yet.")
    else:
        for s in reversed(scores[-6:]):
            if s["intent"] == "evaluator":
                icon = "✅" if "PASS" in s["verdict"].upper() else "❌"
            elif s["intent"] == "hint":
                icon = "💡"
            else:
                icon = "⏱️"
            lang_tag = f"`{s.get('language', 'py')}` " if s.get("language") else ""
            st.caption(f"{icon} {lang_tag}{s['date']}  \n_{s['problem'][:45]}..._")

    st.divider()
    if st.button("🗑️ Clear History", use_container_width=True):
        import os
        if os.path.exists("scores.json"):
            os.remove("scores.json")
        st.success("Cleared!")
        st.rerun()

# ── Main ────────────────────────────────────────────────────────
q    = st.session_state.current_question
lang = st.session_state.selected_language
lang_icon = LANGUAGES[lang]["icon"]
placeholder = LANGUAGES[lang]["placeholder"]

st.title("🧠 Coding Interview Agent")

# Language badge at top
st.markdown(
    f'<span style="background:#f0f2f6;padding:4px 12px;border-radius:20px;font-size:13px;font-weight:500;">'
    f'{lang_icon} {lang}</span>',
    unsafe_allow_html=True
)
st.write("")

# Question card
diff_color = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
icon = diff_color.get(q["difficulty"], "⚪")

with st.container(border=True):
    col_title, col_badge1, col_badge2 = st.columns([4, 1, 1])
    with col_title:
        st.subheader(f"#{q['id']} — {q['title']}")
    with col_badge1:
        st.markdown(f"**{icon} {q['difficulty']}**")
    with col_badge2:
        st.markdown(f"`{q['category']}`")
    st.markdown(q["problem"])

st.divider()

# Code editor
st.subheader(f"✍️ Your {lang} Solution")
user_code = st.text_area(
    "code",
    height=240,
    placeholder=placeholder,
    label_visibility="collapsed"
)

# Action row
col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    hint_level = st.selectbox(
        "hint_level",
        [1, 2, 3],
        format_func=lambda x: {1: "💡 Level 1 — Nudge", 2: "💡 Level 2 — Algorithm", 3: "💡 Level 3 — Pseudocode"}[x],
        label_visibility="collapsed"
    )

with col_b:
    if st.button("💡 Get Hint", use_container_width=True):
        with st.spinner("Thinking..."):
            result = run_agent(q["problem"], user_code, "hint", lang, hint_level)
        st.session_state.hint_result = result
        st.session_state.show_hint   = True
        save_score(q["title"], result, "hint")
        st.rerun()

with col_c:
    if st.button("✅ Evaluate", use_container_width=True):
        if not user_code.strip():
            st.warning("Write some code first!")
        else:
            with st.spinner(f"Evaluating your {lang} solution..."):
                result = run_agent(q["problem"], user_code, "evaluator", lang)
            st.session_state.eval_result = result
            st.session_state.show_eval   = True
            verdict = "PASS" if "PASS" in result.upper() else "FAIL"
            save_score(q["title"], verdict, "evaluator")
            st.rerun()

with col_d:
    if st.button("⏱️ Complexity", use_container_width=True):
        if not user_code.strip():
            st.warning("Write some code first!")
        else:
            with st.spinner("Analyzing complexity..."):
                result = run_agent(q["problem"], user_code, "complexity", lang)
            st.session_state.complexity_result = result
            st.session_state.show_complexity   = True
            save_score(q["title"], result, "complexity")
            st.rerun()

st.divider()

# Results
if st.session_state.show_hint and st.session_state.hint_result:
    with st.container(border=True):
        st.markdown(f"### 💡 Hint for {lang}")
        st.markdown(st.session_state.hint_result)

if st.session_state.show_eval and st.session_state.eval_result:
    with st.container(border=True):
        verdict = "PASS" if "PASS" in st.session_state.eval_result.upper() else "FAIL"
        if verdict == "PASS":
            st.success(f"✅ VERDICT: PASS  ({lang})")
        else:
            st.error(f"❌ VERDICT: FAIL  ({lang})")
        st.markdown(st.session_state.eval_result)

if st.session_state.show_complexity and st.session_state.complexity_result:
    with st.container(border=True):
        st.markdown(f"### ⏱️ Complexity Analysis ({lang})")
        st.markdown(st.session_state.complexity_result)
