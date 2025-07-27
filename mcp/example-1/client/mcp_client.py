import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

#python ./client/mcp_client.py

async def main():
    server_params = StdioServerParameters(
        command=r"D:\Work\miniconda_env\try-mcp-2.x\python",
        args=[r"D:\Work\wsl\Git\LearnAgenticAI\mcp\example-1\server\math_server.py", "stdio"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            llm = ChatOllama(model="llama3.2:3b", temperature=0)
            # create_react_agent is synchronous
            agent = create_react_agent(llm, tools)

            for query in ["What is 7 + 13?", "Compute 6 × 9."]:
                response = await agent.ainvoke({"messages":[{"role":"user","content":query}]})
                #print(f"Response: {response}")
                # Index into the returned dict
                last_msg = response["messages"][-1]
                answer = last_msg["content"] if isinstance(last_msg, dict) else last_msg.content
                print(f"Query: {query}\nAnswer: {answer}\n")

if __name__ == "__main__":
    asyncio.run(main()) 
