"""Tests funcitons in the dictionary.py file."""


__author__ = "730652641"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


#  Tests for invert
def test_invert1() -> None:
    """Tests Edge case (input dict is empty)."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_invert2() -> None:
    """Test use case 1."""
    dict1: dict[str, str] = {"key1": "1", "key2": "2", "key3": "3"}
    assert invert(dict1) == {"1": "key1", "2": "key2", "3": "key3"}


def test_invert3() -> None:
    """Test use case 2."""
    dict1: dict[str, str] = {"1": "key1", "2": "key2", "3": "key3"}
    assert invert(dict1) == {"key1": "1", "key2": "2", "key3": "3"}


#  Tests for favorite_color
def test_fav_col1() -> None:
    """Test edge case (input is empty dict)."""
    empty_dict: dict[str, str] = {}
    assert favorite_color(empty_dict) == ""


def test_fav_col2() -> None:
    """Test use case."""
    dict1: dict[str, str] = {"max": "blue", "john": "yellow", "nathan": "yellow"}
    assert favorite_color(dict1) == "yellow"


def test_fav_col3() -> None:
    """Test use case (input is with capitalized colors)."""
    dict1: dict[str, str] = {"max": "Blue", "john": "Yellow", "nathan": "yellow"}
    assert favorite_color(dict1) == "yellow"


#  Tests for count
def test_count1() -> None:
    """Test edge case (input empty list)."""
    empty: list[str] = []
    assert count(empty) == {}


def test_count2() -> None:
    """Test use case."""
    list1: list[str] = ["max", "max", "max", "john", "adam", "adam"]
    assert count(list1) == {"max": 3, "john": 1, "adam": 2}


def test_count3() -> None:
    """Test use case."""
    list1: list[str] = ["john", "john", "john", "john", "john", "john"]
    assert count(list1) == {"john": 6}


#  Tests for alphabetizer
def test_alpha1() -> None:
    """Test edge case (empty list)."""
    empty: list[str] = []
    assert alphabetizer(empty) == {}


def test_alpha2() -> None:
    """Test use case."""
    list1: list[str] = ["dude", "bro", "broski", "myguy", "dude'et", "bruv", "dog", "myg"]
    assert alphabetizer(list1) == {"d": ["dude", "dude'et", "dog"], "b": ["bro", "broski", "bruv"], "m": ["myguy", "myg"]}


def test_alpha3() -> None:
    """Test use case."""
    list1: list[str] = ["bro", "broski", "myg"]
    assert alphabetizer(list1) == {"b": ["bro", "broski"], "m": ["myg"]}


#  Tests for update_attendance
def test_update_attendance1() -> None:
    """Test edge case (repetition of names in 1 day)."""
    dict1: dict[str, list[str]] = {'Monday': ['Anna']}
    assert update_attendance(dict1, 'Monday', 'Anna') == {'Monday': ['Anna']}


def test_update_attendance2() -> None:
    """Test use case."""
    dict1: dict[str, list[str]] = {'Monday': ['Anna', 'John', 'Adam']}
    assert update_attendance(dict1, 'Monday', 'Joseph') == {'Monday': ['Anna', 'John', 'Adam', 'Joseph']}


def test_update_attendance3() -> None:
    """Test use case."""
    dict1: dict[str, list[str]] = {'Monday': ['Anna', 'John', 'Adam']}
    assert update_attendance(dict1, 'Tuesday', 'Joseph') == {'Monday': ['Anna', 'John', 'Adam'], 'Tuesday': ['Joseph']}