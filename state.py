from typing import TypedDict, Optional, List

class InterviewState(TypedDict):
    problem: str
    user_code: str
    language: str
    hint_level: int
    retrieved_context: str
    hint_output: Optional[str]
    evaluation_output: Optional[str]
    complexity_output: Optional[str]
    messages: List[dict]
    next_agent: str
