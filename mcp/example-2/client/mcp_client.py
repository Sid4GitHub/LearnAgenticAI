from langchain_mcp_tools import convert_mcp_to_langchain_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
import asyncio

# python ./client/mcp_client.py

async def main():
    # NOTE: No need to instantiate fastmcp.Client here
    # convert_mcp_to_langchain_tools will handle servers for you
    tools, cleanup = await convert_mcp_to_langchain_tools({
        "math": {
            "url": "http://localhost:8000/mcp/",
            "transport": "streamable-http",
        }
    })

    llm   = ChatOllama(model="llama3.2:3b", temperature=0)
    agent = create_react_agent(llm, tools)

    # Example queries
    for query in ["What is 7 + 13?", "Compute 6 × 9."]:
        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": query}]}
        )
        last   = result["messages"][-1]
        answer = last.get("content") if isinstance(last, dict) else last.content
        print(f"Query: {query}\nAnswer: {answer}\n")

    # Clean up MCP server sessions
    await cleanup()

if __name__ == "__main__":
    asyncio.run(main())
