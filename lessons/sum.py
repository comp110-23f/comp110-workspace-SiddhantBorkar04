"""Summing the elements of a list using different loops."""

__author__ = "730652641"


def w_sum(vals: list[float]) -> float:
    """Uses while loop to return total."""
    i: int = 0
    final_val: float = 0.0
    while (i < len(vals)):
        final_val += vals[i]
        i += 1
    return final_val


def f_sum(vals: list[float]) -> float:
    """Uses for loop to return total."""
    final_val: float = 0.0
    for i in vals:
        final_val += i 
    return final_val


def f_range_sum(vals: list[float]) -> float:
    """Uses for loop with range loop to return total."""
    final_val: float = 0.0
    for i in range(len(vals)):
        final_val += vals[i] 
    return final_val