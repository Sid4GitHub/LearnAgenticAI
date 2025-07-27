from langchain_mcp_tools import convert_mcp_to_langchain_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent 
from langchain_mcp_tools import convert_mcp_to_langchain_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
import subprocess 
import asyncio

# python ./client/mcp_client.py

async def main():
    server_configs = {
        "add_tool": {
            "command": "D:\\Work\\miniconda_env\\try-mcp-2.x\\python.exe",
            "args": ["D:\\Work\\wsl\\Git\\LearnAgenticAI\\mcp\\example-3\\server\\add_server.py"],
            "transport": "stdio",
            "errlog": subprocess.DEVNULL 
        },
        "multiply_tool": {
            "url": "http://127.0.0.1:8000/mcp",
            "transport": "streamable-http",
            "errlog": subprocess.DEVNULL 
        }
    }

    tools, cleanup = await convert_mcp_to_langchain_tools(server_configs)


    print("Available tools:", tools)

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
