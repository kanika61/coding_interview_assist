from langgraph.graph import StateGraph, END
from state import InterviewState
from agents.hint_agent import hint_agent
from agents.evaluator_agent import evaluator_agent
from agents.complexity_agent import complexity_agent
from retrieval.chroma_store import retrieve_context

def retrieval_node(state: InterviewState) -> InterviewState:
    print("[retrieval] Fetching relevant DSA context...")
    context = retrieve_context(state["problem"])
    return {**state, "retrieved_context": context}

def route_after_retrieval(state: InterviewState) -> str:
    return state["next_agent"]

def build_graph():
    workflow = StateGraph(InterviewState)

    workflow.add_node("retrieval",  retrieval_node)
    workflow.add_node("hint",       hint_agent)
    workflow.add_node("evaluator",  evaluator_agent)
    workflow.add_node("complexity", complexity_agent)

    workflow.set_entry_point("retrieval")

    workflow.add_conditional_edges(
        "retrieval",
        route_after_retrieval,
        {
            "hint":       "hint",
            "evaluator":  "evaluator",
            "complexity": "complexity",
        }
    )

    workflow.add_edge("hint",       END)
    workflow.add_edge("evaluator",  END)
    workflow.add_edge("complexity", END)

    return workflow.compile()

app = build_graph()
