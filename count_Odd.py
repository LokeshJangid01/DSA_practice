"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

def count_odds(low: int, high: int) -> int:
    # Calculate the number of odd numbers between low and high
    return (high + 1) // 2 - low // 2

