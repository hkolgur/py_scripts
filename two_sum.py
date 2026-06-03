"""find indices of 2 elements of a lits that add up to a target number"""

num = [1, 2, 3, 5, 10]
target = 7

# --------solution 1-Brute force-------------
result = []

for i, n1 in enumerate(num):
    for j, n2 in enumerate(num[i + 1 :], start=i + 1):
        if (num[i] + num[j]) == target:
            result.append([i, j])

print((result))
d1 = {}
result1 = []
# --------solution 2 optimal--------------
print("solution 2")
for i, ele in enumerate(num):
    compliment = target - ele
    if compliment in d1:
        result1.append([d1[compliment], i])
        print(result1)
    else:
        d1[ele] = i
        print(d1)

print(result1[0])
