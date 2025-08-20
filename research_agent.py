from typing import List, TypedDict
from langchain_core.messages import BaseMessage

class ResearchState(TypedDict):
    messages: List[BaseMessage]
    user_query: str
    research_plan: List[str]
    search_results: List[str]
    summary: str
    citations: List[str]
