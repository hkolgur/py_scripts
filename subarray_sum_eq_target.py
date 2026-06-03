"""find a sub array in given non-negative array that has sum equal to given target sum.
Sliding window with variable size"""

n = [3, 1, 3, 9, 2, 1, 7, 5]  # 3,4 /5, 2/ 7 /-1,8
target_sum = 10
length = len(n)
start = 0
result = []
curr_sum = 0

for end in range(length):
    curr_sum += n[end]
    # print("1 curr_sum", curr_sum)
    while curr_sum > target_sum:
        curr_sum -= n[start]
        start += 1
    if curr_sum == target_sum:
        result.append([start, end])
print(result)
# return longest =-1 if no match else return the maximum substring length .
longest = -1
for element in result:
    longest = max(
        longest, ((element[1] - element[0]) + 1)
    )  # +1 for end - start to make it inclusive
print(longest)
