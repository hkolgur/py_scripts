"""Maximum sum of subarry of any size. Return only the maxsum no need of indices"""

nums = [1, 9, -2, 3, -14, 5, 3]
curr_sum = 0
max_sum = nums[0]
for ele in nums:
    curr_sum = max(curr_sum,0)
    curr_sum +=ele
    max_sum = max(max_sum, curr_sum)

print(max_sum)
