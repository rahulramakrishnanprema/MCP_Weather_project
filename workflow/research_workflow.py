from langgraph.graph import StateGraph, END
from agents.manager_agent import ManagerAgent, ResearchState
from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.reviewer_agent import ReviewerAgent

def create_research_workflow():
    workflow = StateGraph(ResearchState)

    # Define the nodes
    workflow.add_node("manager", ManagerAgent().route_query)
    workflow.add_node("planner", PlannerAgent().generate_research_plan)
    workflow.add_node("researcher", ResearcherAgent().execute_search)
    workflow.add_node("reviewer", ReviewerAgent().review_and_summarize)

    # Set the entry point
    workflow.set_entry_point("manager")

    # Define the edges
    workflow.add_edge("manager", "planner")
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "reviewer")

    # Define the conditional edge for data evaluation loop
    # For simplicity, we'll assume research is complete after one cycle for now.
    # In a real scenario, this would involve a more complex evaluation.
    workflow.add_edge("reviewer", END)

    return workflow.compile()

