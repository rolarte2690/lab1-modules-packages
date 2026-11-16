import math


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Python modules and packages."


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)
