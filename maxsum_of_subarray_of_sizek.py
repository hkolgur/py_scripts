"""compute max sum of a sub array of sike k in an array of size n"""

n = [2,-6,3,4,-5]
k = 4
length = len(n)
if length >= k:
    curr_sum = sum(n[:k])
    max_sum = curr_sum
    for i in range(length - k):
        # subtract leaving ele from window and add next element entering window
        curr_sum = max_sum + n[i + k] - n[i]
        max_sum = max(max_sum, curr_sum)
    print("maximum sum of of subarray is ", max_sum)
else:
    print("Main Arry size is less than subarry size")
