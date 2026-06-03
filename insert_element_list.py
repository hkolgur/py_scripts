"""insert element in specified position"""

nums = [70, 60, 50, -1]

element = 40
pos = 4

if nums[pos - 1] == -1:
    nums[pos - 1] = element
else:
    nums.insert(pos - 1, element)
    if nums[-1]==-1:
        nums.pop()

print(nums)
