from transformers import pipeline
from typing import List, TypedDict

class ResearchState(TypedDict):
    query: str
    research_plan: List[str]
    research_results: List[str]
    final_summary: str

class PlannerAgent:
    def __init__(self):
        self.llm = pipeline("text-generation", model="distilbert/distilgpt2") # Using a small, local LLM for planning

    def generate_research_plan(self, state: ResearchState) -> ResearchState:
        # Simulate LLM generating a research plan and search queries
        plan = [f"Search for: {state['query']} history", f"Search for: {state['query']} current events"]
