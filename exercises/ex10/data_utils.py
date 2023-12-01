"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730652641"


"""Working with CSV Data."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_vals(table, key)
    return result


def head(dict1: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Returns given number of first values of the column."""
    final: dict[str, list[str]] = {}
    for key, val in dict1.items():
        list1: list[str] = []
        for n in range(min(num, len(val))):
            list1.append(val[n])
        final[key] = list1
    return final


def select(dict1: dict[str, list[str]], list1: list[str]) -> dict[str, list[str]]:
    """Returns selected columns only."""
    final: dict[str, list[str]] = {}
    for i in list1:
        final[i] = dict1[i]
    return final


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatinates 2 tables together."""
    final: dict[str, list[str]] = {}
    for i in dict1:
        final[i] = dict1[i]
    for n in dict2:
        if n in final:
            final[n].extend(dict2[n])
        else:
            final[n] = dict2[n]
    return final


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of instances of each element in the list."""
    final: dict[str, int] = {}
    for curr in list:
        if curr in final:
            final[curr] += 1
        else:
            final[curr] = 1
    return final