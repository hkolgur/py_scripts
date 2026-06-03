"""illustrate mutable vs immutable"""


def get_largest_numbers(numbers: list, topn: int) -> list:
    """returns topn largest numbers"""
    numbers.sort()
    return numbers[-topn:]


num = [34, 5, 20, 34, 12, 24]
print(f'Initial List:{num}')
top_n_largest=get_largest_numbers(num, 3)
print(f'Final  List: {num}')
