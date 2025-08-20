from langchain_core.messages import BaseMessage
from typing import List, Tuple, Annotated, TypedDict

class ResearchState(TypedDict):
    query: str
    research_plan: List[str]
    research_results: List[str]
    final_summary: str

class ManagerAgent:
