"""Combining two lists into a dictionary."""

__author__ = "730652641"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Combines str list and int list into a dictionary."""
    if (len(str_list) != len(int_list)):
        return dict()
    final_dict = dict()
    for i in range(len(str_list)):
        final_dict[str_list[i]] = int_list[i]
    return final_dict