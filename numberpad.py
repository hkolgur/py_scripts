"""Design a dial pad"""

pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

for row in pad:
    for num in row:
        print(num, end=" ")
    print()

# print([num for row in pad [for num in row]])
print([num for row in pad for num in row])

[[print(num, end=" ") for num in row] and print() for row in pad]
 