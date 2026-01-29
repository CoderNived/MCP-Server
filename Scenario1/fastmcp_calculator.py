import numpy as np
from fastmcp import FastMCP

mcp = FastMCP(name = 'FastMCP Calculator')

@mcp.tool
def multiply(a: float, b:float)-> float:
    return a*b

# @mcp.tool
# def add(a: float, b:float) -> float:
#     return a+b
@mcp.tool(
    name = 'add',
    description = "Add Two Numbers"
) 
def add(a: float, b:float) -> float:
    return a+b
