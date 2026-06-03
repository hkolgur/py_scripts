"""Intersection of two arrays"""

from collections import Counter

list1 = [7, 7, 14, 92, 14, 92, 92]
list2 = [0, 0, 92, 92, 7]
result = []
# ----------solution 1----------------------
# for ele in list1:
#     if ele in list2:
#         if (Counter(result).get(ele) is None) or (
#             Counter(result).get(ele)
#             < (Counter(list1).get(ele) and Counter(list2).get(ele))
#         ):
#             result.append(ele)
# ----------solution 2----------------------
allowed_counts = Counter(list2)
for ele in list1:
    if allowed_counts[ele] > 0:
        result.append(ele)
        allowed_counts[ele] -= 1
# --------------------------------
print(result)

#------alt approch eleminates dups, do not preserve order---------
res= list(set(list1)&set(list2))
print(f'set intersection{res}')

# def find_intersection(list_1: list, list_2: list):
#     """find common elements"""
#     result = [ele for ele in list_1 if ele in list_2]
#     return result


# result_list = find_intersection(list1, list2)
# print(f"resut:{result_list}")
