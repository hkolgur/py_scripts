"""Test"""
a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))

try:
    result=a/b
except ZeroDivisionError:
    print("Second number is zero division not possible")
else:
    print("Result of division is",result)
finally:
    print("Always runs")