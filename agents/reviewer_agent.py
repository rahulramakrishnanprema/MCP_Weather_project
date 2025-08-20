from typing import List, TypedDict

class ResearchState(TypedDict):
    query: str
    research_plan: List[str]
    research_results: List[str]
    final_summary: str

class ReviewerAgent:
    def __init__(self):
        pass

    def review_and_summarize(self, state: ResearchState) -> ResearchState:
        # Simulate reviewing and summarizing research data
