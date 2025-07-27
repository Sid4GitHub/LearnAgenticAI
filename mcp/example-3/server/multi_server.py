from fastmcp import FastMCP

# python .\server\multi_server.py
# npx @modelcontextprotocol/inspector

mcp = FastMCP("Math")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

if __name__ == "__main__":
     # transport must be "stdio" to work with MCPO
    mcp.run(transport="http", host="0.0.0.0", port=8000)
