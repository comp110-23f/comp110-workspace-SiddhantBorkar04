"""Assignment of learning how to use dictionaries."""


__author__ = "730652641"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    # Checks for KeyError
    kill: bool = False
    for key in dict1:
        ref: int = 0
        for key2 in dict1:
            if (dict1[key] == dict1[key2]):
                ref += 1
            if (ref > 1):
                kill = True
        ref = 0
    if (kill):
        raise KeyError("A Key is repeated. Please ensure all Keys are different!")

    final_dict: dict[str, str] = {}
    for key in dict1:
        final_dict[dict1[key]] = key
    return final_dict


def favorite_color(dict: dict[str, str]) -> str:
    """Prints the most commonly referenced color."""
    list_colors: list[str] = list()
    for key in dict:
        list_colors.append(dict[key])

    most_refs: int = 0
    current_ref: int = 0
    current_color: str = ""
    most_color: str = ""
    for i in list_colors:
        current_color = i
        current_ref = 0
        for n in list_colors:
            if (i == n):
                current_ref += 1
        if (current_ref > most_refs):
            most_refs = current_ref
            most_color = current_color
    return most_color


def count(og_list: list[str]) -> dict[str, int]:
    """Counts number of str instances in list, and returns dict with associated counts."""
    final_dict: dict[str, int] = {}
    i: int = 0
    while i < len(og_list):
        if og_list[i] in final_dict:
            final_dict[og_list[i]] += 1
        else:
            final_dict[og_list[i]] = 1
        i += 1
    return final_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Takes a list of str and returns dict with key of each first letter, and values of each str having the first letter."""
    final_dict: dict[str, list[str]] = {}
    i: int = 0
    current_first_letter: str = ""
    while i < len(list1):
        current_first_letter = list1[i][0].lower()
        if current_first_letter in final_dict:
            final_dict[current_first_letter].append(list1[i])
        else:
            final_dict[current_first_letter] = [list1[i]]
        i += 1
    return final_dict


def update_attendance(og_dict: dict[str, list[str]], week_day: str, attend_student: str) -> dict[str, list[str]]:
    """Adds new students who have attended class to the day keys of dictionary."""
    og_dict_update = og_dict
    if week_day in og_dict_update:
        og_dict_update[week_day].append(attend_student)
    else:
        og_dict_update[week_day] = [attend_student]
    return og_dict_update