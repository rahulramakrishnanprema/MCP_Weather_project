from typing import List, TypedDict, Annotated, Union
from langchain_core.messages import BaseMessage

from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient

class ResearchState(TypedDict):
    messages: List[BaseMessage]
    user_query: str
    research_plan: List[str]
    search_results: List[str]
    summary: str
    citations: List[str]

# Initialize HuggingFace LLM
llm = init_chat_model("HuggingFaceH4/zephyr-7b-beta")

# Configure MultiServerMCPClient
client = MultiServerMCPClient(
    {
        "research_tools": {
            "command": "python",
            "args": ["./research_tools_server.py"],
            "transport": "stdio",
        }
    }
)

def manager_agent(state: ResearchState) -> ResearchState:
    """Entry point for user queries, initializes state and routes to planner_agent."""
    user_query = state["user_query"]
    messages = state.get("messages", []) + [("user", user_query)]
    return {"user_query": user_query, "messages": messages}

from pydantic import BaseModel, Field

class ResearchPlan(BaseModel):
    """A detailed research plan with steps and search queries."""
    plan: List[str] = Field(description="List of research steps and corresponding search queries.")

def planner_agent(state: ResearchState) -> ResearchState:
    """Generates a research plan based on the user query."""
    user_query = state["user_query"]
    prompt = PromptTemplate.from_template(
        """You are a research planner. Based on the user's query, generate a detailed research plan.
        The plan should include a list of steps and specific search queries for each step.
        User query: {user_query}
        """
    )
    # Ensure the LLM is configured for structured output
    structured_llm = llm.with_structured_output(ResearchPlan)
    
    chain = {"user_query": RunnablePassthrough()} | prompt | structured_llm
    
    research_plan_obj = chain.invoke(user_query)
    research_plan = research_plan_obj.plan
    
    return {"research_plan": research_plan, "messages": state["messages"] + [("assistant", f"Research plan generated: {research_plan}")]}

async def researcher_agent(state: ResearchState) -> ResearchState:
    """Iterates through the research plan, performs web searches, and collects results."""
    research_plan = state["research_plan"]
    search_results = state.get("search_results", [])
    messages = state["messages"]

    # Get the perform_web_search tool from the client
    tools = await client.get_tools()
    perform_web_search_tool = next((t for t in tools if t.name == "perform_web_search"), None)

    if not perform_web_search_tool:
        raise ValueError("perform_web_search tool not found.")

    for query in research_plan:
        # Simulate calling the tool via ToolNode or directly if possible
        # For simplicity, directly calling the tool function here.
        # In a real LangGraph setup, this would be handled by a ToolNode.
        result = perform_web_search_tool.invoke({"query": query})
        search_results.append(result)
        messages.append(("assistant", f"Search for '{query}' completed."))

    return {"search_results": search_results, "messages": messages}




