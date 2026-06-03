"""Pivot index in array. If there are multiple indices return them.
A pivot index is an array position where the sum of all elements 
strictly to its left equals the sum of all elements strictly to its right"""

list = [0, 1, -1]

pivot = []
len = len(list)
print("len of list", len)
for i in range(len):
    if (sum(list[0:i])) == (sum(list[i + 1 : len])):
        pivot.append(i)

print(f"pivot is {pivot}")
