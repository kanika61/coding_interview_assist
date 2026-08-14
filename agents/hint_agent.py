from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.2", temperature=0.3)

def hint_agent(state: dict) -> dict:
    level = state.get("hint_level", 1)
    language = state.get("language", "python")

    level_instructions = {
        1: "Give a very gentle conceptual nudge. Do NOT mention the algorithm or data structure by name. Just point the user towards a way of thinking.",
        2: "Name the algorithm or data structure they should use. Explain why it fits this problem. Do NOT write any code.",
        3: f"Give near-solution pseudocode or a code skeleton in {language}. Walk through the approach step by step clearly."
    }

    system_prompt = f"""You are a friendly coding interview coach helping a candidate work through a DSA problem.
The candidate is coding in {language}. Tailor your hint to {language} conventions and syntax.
Your job is to give a level {level} hint.

Hint level instructions:
{level_instructions[level]}

Relevant DSA concepts from knowledge base:
{state.get('retrieved_context', 'None retrieved.')}

Be encouraging. Keep the response concise, under 150 words.
"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""
Problem:
{state['problem']}

User's current {language} code:
{state['user_code'] or f'No code written yet. They are using {language}.'}
""")
    ])

    return {**state, "hint_output": response.content}
