"""compute the sum of for sub array of size k that matches a given target sum
return the total number of subarrays that matches this critera"""

n = [2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4]
target = 7
k = 3
count = 0
lenght = len(n)
if lenght >= k:
    curr_sum = sum(n[:k])
    if curr_sum == target:
        count += 1
    for i in range(lenght - k):
        curr_sum = curr_sum - n[i] + n[i + k]
        if curr_sum == target:
            count += 1
    print(f"Total number of sub arrays with target sum of:{target} are:{count}")
else:
    print("size of sub array is less than the size of original array")
