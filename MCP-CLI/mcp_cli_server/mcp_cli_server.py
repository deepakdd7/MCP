# Module Import
import sys
#from typing import Any
from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP("MCP Calculator")
print("Server env is :: ", sys.prefix)


# MCP tool to add two integer numbers
@mcp.tool()
async def add_numbers(num1: int, num2:int) -> int:
    """Add Two numbers

    Args:
        num1: First Integer Number
        num2: Second Integer Number

    Returns:
        int: Addition of two numbers
    """
    return num1 + num2


# MCP tool to multipley two integer numbers
@mcp.tool()
async def multiply_numbers(num1: int, num2:int) -> int:
    """Multiply Two numbers

    Args:
        num1: First Integer  Number
        num2: Second Integer Number


    Returns:
        int: Multiplication of two numbers
    """

    return num1 * num2


if __name__ == "__main__":
    # Initialize and run the server
    print("Server env is ", sys.prefix)
    mcp.run(transport='stdio')
