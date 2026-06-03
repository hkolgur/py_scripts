"""Demonstrate List comprehensions"""

from pprint import pprint

nums = [x for x in range(1, 10)]
print("Single List Comprehension", nums)

even = [x for x in range(1, 10) if x % 2 == 0]
print("Single List Comprehension with condition", even)

loop_value = [[x + y for x in range(1, 3) for y in range(1, 3)]]
print("Multi list comprehension:", loop_value)

# 1.names starts with a and ends with y
names = ["alice", "burbon", "cutter", "arnold", "anthony", "Andy", " ", "a"]
new_names = [
    name
    for name in names
    if name.lower().startswith("a") and name.lower().endswith("y")
]
print(f"Names that start with A and ends in y:{new_names}")

# 2. second method
new_names1 = [
    name
    for name in names
    if len(name) >= 1
    if name.lower().startswith("a")
    if name.lower().endswith("y")
]
print(f"Option 2..{new_names1}")

# flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend = [num for row in matrix for num in row]
print(f"flattened matrix:{flattend}")

# categorize number inot even or odd from 0 through 10
category = ["even" if num % 2 == 0 else "odd" for num in range(10)]
print(f"category values:{category}")

# Build 3d list
lst = [[[num for num in range(3)] for _ in range(3)] for _ in range(3)]
pprint(lst)


# Transformation in comprehension
def square(x: int) -> int:
    """Retruns square of a number"""
    return x**2


def valid_evens(x: int) -> bool:
    """Retruns True for even numbers"""
    return x % 2 == 0


squares = [square(x) for x in range(5) if valid_evens(x)]
print(squares)

# Dictionary comprehension
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}
print(my_dict)

# set comprehension
numbs = [
    1,
    2,
    2,
    3,
    3,
    3,
    4,
]

unique_squares = {v**2 for v in numbs}
print(unique_squares)

# Generator comprehension
# Generator: Gives one value at a time when requested instead of giving
#           million at once
Sum_of_squares_as_generator = sum(x**2 for x in range(10))
print(Sum_of_squares_as_generator)
Sum_of_squares_normal = sum([x**2 for x in range(10)])
print(Sum_of_squares_normal)
