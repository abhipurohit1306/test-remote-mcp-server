from fastmcp import FastMCP
import random
import json

#create the fastMCP instance
mcp = FastMCP("Simple Calculator Server")

#tool: Add 2 numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

#Tool: Generate a random number
@mcp.tool
def generate_random_number(min_val: int=1, max_val: int=100) -> int:
    """Generate a random number between min_val and max_val.

    Args:
        min_val (int): The minimum value (default = 1).
        max_val (int): The maximum value (default = 100).
    Returns:
        int: A random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)

#Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""

    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Abhishek"
    }
    return json.dumps(info, indent=2)

#Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)