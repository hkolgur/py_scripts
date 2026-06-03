"""sort strings based on length"""


def sort_fn(lst: list) -> list:
    """return sorted strings"""
    d1 = [[st, len(st)] for st in lst]
    d1.sort(key=lambda x:x[1])
    return d1


str_1 = ["hi", "hello", "bye"]
str_2 = ["helloo", "you", "r", "crazy"]
print(sort_fn(str_1))

# solution 1
str_2.sort(key=len)
print(f"solution 1: {str_2}")
