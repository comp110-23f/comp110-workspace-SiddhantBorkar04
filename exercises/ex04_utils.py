"""EX04 - Utils."""


__author__ = "730652641"


def max(input: list[int]) -> int:
    """Returns the max value in the input list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    n: int = 0
    large: int = input[0]
    while (n < len(input)):
        if (large < input[n]):
            large = input[n]
        n += 1
    return large


def is_equal(intList1: list[int], intList2: list[int]) -> bool:
    """Returns true if lists are the same."""
    n: int = 0
    if (len(intList1) != len(intList2)):
        return False
    while (n < len(intList1)):
        if (intList1[n] != intList2[n]):
            return False
        n += 1
    return True


def all(intList: list[int], x: int) -> bool:
    """Returns true if input int is in input list."""
    if (len(intList) == 0):
        return False
    n: int = 0
    while (n < len(intList)):
        if (intList[n] != x):
            return False
        n += 1
    return True