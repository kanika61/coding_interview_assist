from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.2", temperature=0)

def complexity_agent(state: dict) -> dict:
    language = state.get("language", "python")

    system_prompt = f"""You are an algorithms expert explaining time and space complexity.
The code is written in {language}. Reference {language}-specific data structures where relevant
(e.g. Python dict is O(1) average, Java HashMap is O(1) average, C++ unordered_map is O(1) average).

Analyze the given code and provide:
1. TIME COMPLEXITY: identify each loop, recursive call, or operation. Give Big-O for best, average, and worst case.
2. SPACE COMPLEXITY: identify all data structures allocated. Give Big-O.
3. EXPLANATION: walk through the reasoning in plain English.
4. OPTIMAL: what is the best achievable complexity for this problem? Is this solution optimal?

Be precise and educational.
"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""
Problem:
{state['problem']}

Language: {language}

Code:
{state['user_code']}
""")
    ])

    return {**state, "complexity_output": response.content}
