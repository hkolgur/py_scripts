"""Maximum sum of subarry of any size. Return  indices"""

nums = [1, 9, -2, 3, -14, 5, 3]
curr_sum = 0
max_sum = nums[0]
start=0
end=0
temp_start=0
for i,ele in enumerate(nums):
    if curr_sum < 0:
        curr_sum=ele 
        temp_start=i
    else:
        curr_sum +=ele

    if curr_sum > max_sum:
        max_sum=curr_sum
        start =temp_start
        end=i
      

print(max_sum,start,end)
