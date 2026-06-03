"""Reverese an array"""


# def reverse_array_builtin(numsl: list) -> list:
#     """Reverse an array"""
#     numsl.reverse()
#     return numsl


def reverse_array_custom(my_list):
    """custom reverse"""
    start = 0
    last = len(my_list) - 1
    for _ in range(int(len(my_list) / 2)):
        my_list[start], my_list[last] = my_list[last], my_list[start]
        start += 1
        last -= 1
    return my_list


# nums_builtin = [10, 20, 30, 40, 50]
nums_custom = [10, 20, 30, 40, 50]
# print(f"Original List before inbuilt reverse:{nums_builtin}")
# reversed_list_builtin = reverse_array_builtin(nums_builtin)
# print(f"reversed list after built in function:{reversed_list_builtin}")

print(f"Original List before custom reverse:{nums_custom}")
reversed_list_custom = reverse_array_custom(nums_custom)
print(f"reversed list after custom in function:{reversed_list_custom}")
