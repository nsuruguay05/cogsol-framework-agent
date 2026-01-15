from mcp.server.fastmcp import FastMCP

from agents.cogsolframeworkagent import CogsolFrameworkAgent
from data.retrievals import CogsolFrameworkDocsRetrieval

mcp = FastMCP("CogSol Framework Assistant", port=8008)
_agent = CogsolFrameworkAgent()
_retrieval = CogsolFrameworkDocsRetrieval()


@mcp.tool()
def ask_cogsol_framework(question: str, reset: bool = False) -> str:
    """Ask the CogSol Framework agent a question."""
    response = _agent.run(question, reset=reset)
    messages = response.get("messages", [])
    if not messages:
        return ""
    return messages[-1].get("content", "")

@mcp.tool()
def search_framework_docs(question: str) -> str:
    """Search the CogSol Framework documentation."""
    results = _retrieval.run(question)
    similar_blocks = results.get("similar_blocks", [])
    if not similar_blocks:
        return "No relevant documentation found."
    return "\n\n".join(f"- {block['source']}:\n\"{block['text']}\"" for block in similar_blocks)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
