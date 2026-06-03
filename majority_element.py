"""If an element appears more than half the times in the array,its Majority element"""

from collections import Counter

num = [3, 3, 3, 2, 2, 2, 3]

num_counter = Counter(num)

if len(set(num)) > len(num) / 2:
    print("Majority Element do not exist in given array")
else:
    print(
        num_counter.most_common(1)
    )  # returns top 1 most common elements which is tupple
    print(
        num_counter.most_common(1)[0][0]
    )  # tupple's first element is number,second is times
