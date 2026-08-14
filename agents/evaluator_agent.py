from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.2", temperature=0)

def evaluator_agent(state: dict) -> dict:
    language = state.get("language", "python")

    language_notes = {
        "python":     "Check for Pythonic style: list comprehensions, built-ins, clean naming.",
        "javascript": "Check for proper use of const/let, arrow functions, and JS built-in array methods.",
        "typescript": "Check for proper types, interfaces, and TypeScript best practices.",
        "java":       "Check for proper class structure, access modifiers, and Java conventions.",
        "c++":        "Check for proper use of STL, memory management, and C++ conventions.",
        "c":          "Check for memory management, pointer usage, and C conventions.",
        "go":         "Check for idiomatic Go: error handling, goroutines if relevant, clean naming.",
        "rust":       "Check for ownership rules, borrowing, and idiomatic Rust patterns.",
        "kotlin":     "Check for idiomatic Kotlin: null safety, extension functions, data classes.",
        "swift":      "Check for Swift conventions: optionals, guard statements, value types.",
        "ruby":       "Check for idiomatic Ruby: blocks, built-in enumerable methods, clean style.",
        "php":        "Check for modern PHP conventions, type hints, and clean structure.",
    }

    lang_note = language_notes.get(language.lower(), f"Evaluate using {language} best practices.")

    system_prompt = f"""You are a senior software engineer reviewing a coding interview solution written in {language}.

{lang_note}

Evaluate the solution on these criteria:
1. Correctness: does it solve the problem for all cases?
2. Edge cases: empty input, single element, duplicates, negatives, large input?
3. Code quality: readable, clean, idiomatic {language}?
4. Optimality: is there a better time or space complexity approach?

Format your response exactly like this:
VERDICT: PASS or FAIL
CORRECTNESS: ...
EDGE CASES: ...
CODE QUALITY: ...
BETTER APPROACH: ...
OVERALL FEEDBACK: ...
"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""
Problem:
{state['problem']}

Language: {language}

Solution:
{state['user_code']}
""")
    ])

    return {**state, "evaluation_output": response.content}
