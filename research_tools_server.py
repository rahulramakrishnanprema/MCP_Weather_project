from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ResearchTools")

@mcp.tool()
def perform_web_search(query: str) -> str:
    """Performs a web search and returns the results."""
    print(f"Performing web search for: {query}")
    return f"Search results for '{query}': [Simulated results]"

@mcp.tool()
def validate_data(data: str) -> bool:
    """Validates the given data."""
    print(f"Validating data: {data}")
    return True

if __name__ == "__main__":
