"""find the position of first occurance of a character.If none return -1"""


def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    for i, ch in enumerate(s):
        if ch == to_find:
            return i
    return -1


target = "a"
my_str = "teradata"
print("Position of {target} is:", find_first_occurrence(my_str, target))
