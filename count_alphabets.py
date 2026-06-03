"""count occurance of each apphabet in a string"""

from collections import Counter


# my_keys = set(str_name.lower())
# for k in my_keys:
#     print(k)
def alpha_count_case_insensitive(str_name):
    """Takes string input and gives total alpha counts ignoring the case.
    Returns count of all the alphabets"""
    my_dict = {}
    str_name_counter = Counter(str_name.lower())
    # print(type(str_name_counter))
    for k, v in str_name_counter.items():
        if k.isalpha():
            my_dict[k] = v
    return sum(my_dict.values())


def alpha_count_alternate(str_name):
    """Takes string input and gives total alpha counts ignoring the case.
    Returns count of all the alphabets"""
    count = 0
    for ch in str_name:
        if ch.isalpha():
            count += 1
    return count


# print(my_dict)
str_name = "Mmy name is Hari"
print("Total alphabets", alpha_count_case_insensitive(str_name))
print("Total alphabets second implementation :", alpha_count_alternate(str_name))
