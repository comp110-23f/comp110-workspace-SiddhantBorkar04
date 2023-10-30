"""Test my zip function."""


__author__ = "730652641"

from zip import zip


def test_empty() -> None:
    """Zip funciton of empty lists."""
    str_list: list[str] = []
    int_list: list[int] = []
    assert zip(str_list, int_list) == dict()


def test_1() -> None:
    """Zip function tested with dictionary lenth 1."""
    str_list: list[str] = ["Happy"]
    int_list: list[int] = [1]
    assert len(zip(str_list, int_list)) == 1


def test_2() -> None:
    """Zip function tested with dictionary lenth 2."""
    str_list: list[str] = ["Happy", "Tuesday"]
    int_list: list[int] = [1, 2]
    assert len(zip(str_list, int_list)) == 2