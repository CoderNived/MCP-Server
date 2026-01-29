import numpy as np
import math
from fastmcp import FastMCP

mcp = FastMCP(name="FastMCP Calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
    return a * b

@mcp.tool(name="add", description="Add Two Numbers")
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(a: float, b: float) -> float:
    return a ** b

@mcp.tool()
def sqrt(a: float) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return np.sqrt(a)

@mcp.tool()
def logarithm(a: float, base: float = 10) -> float:
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return np.log(a) / np.log(base)

@mcp.tool()
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Factorial requires an integer")
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

@mcp.tool()
def sine(angle_in_degrees: float) -> float:
    return np.sin(np.radians(angle_in_degrees))

@mcp.tool()
def cosine(angle_in_degrees: float) -> float:
    return np.cos(np.radians(angle_in_degrees))

@mcp.tool()
def tangent(angle_in_degrees: float) -> float:
    if angle_in_degrees % 180 == 90:
        raise ValueError("Tangent undefined at 90° + k·180°")
    return np.tan(np.radians(angle_in_degrees))

@mcp.tool()
def exponential(a: float) -> float:
    return np.exp(a)

@mcp.tool()
def absolute(a: float) -> float:
    return np.abs(a)

if __name__ == "__main__":
    mcp.run()
