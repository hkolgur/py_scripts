"""Demonstrate various parameters to functions"""


def func_add(x, y, z):
    """Add positional paramaters"""
    print(x + y + z)


def func_sub(x, y=0):
    """Add positional and default paramaters"""
    print(x - y)


def func_optional(x, y=None):
    """Add positional optional paramater"""
    print(f"x is:{x}and y is:{y}")


def func_args(x, y, *args):
    """args paramater"""
    print(f"x:{x},y:{y},*args{args}")


def func_kwargs(x, y, **kwargs):
    """kwargs paramater"""
    print(f"x:{x},y:{y},*kwargs{kwargs}")


def func_args_kwargs(*args, **kwargs):
    """args and kwargs paramater"""
    print(f"*args{args},*kwargs{kwargs}")

if __name__=='__main__': #run below code only if its ran directly not in imports

    func_add(1, 2, 3)

    func_add(y=2, x=1, z=3)  # change order but assign values

    func_add(1, z=3, y=2)  # pos and keyword arg combo. pos parm first only.

    func_sub(3)  # default vlaue for second parameter

    func_optional(3)  # optional parameter

    func_args(1, 2, 3, 4, 5)  # args output stored in tupple which is immutable

    # c , d are keys and values are list and dict. kwargs o/p stored in dict
    func_kwargs(1, 2, c=[3, 4], d={"a": "1", "b": "2"})

    # args & kwargs pass positional args in a list
    func_args_kwargs(1, 2, c=[3, 4], d={"a": "1", "b": "2"})

    func_add(*[1, 2, 3])  # passes each value in list as 1 pos parm using *

    func_kwargs(1, 2, **{"c": "[3,4]", "d": "hello"})  # pass kwargs in dict using **
