from fastmcp import FastMCP

#mcpo --host 0.0.0.0 --port 8000 -- python .\server\math_server.py

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

if __name__ == "__main__":
    # Use stdio transport for simplicity
    mcp.run(transport="stdio")
