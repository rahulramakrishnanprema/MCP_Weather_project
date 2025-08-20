from typing import List, TypedDict
from langchain_core.messages import BaseMessage

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

