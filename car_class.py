"""Module to generate cars"""

from typing import Self  # To Annotate Self object in Car method


class Car:
    """ "Car class to generate cars"""

    def __init__(self, brand: str, hp: int) -> None:
        self.brand = brand
        self.hp = hp

    def drive(self) -> None:
        """drive functionality"""
        print(f"{self.brand} is driving")

    def get_info(self) -> None:
        """Car Information"""
        print(f"{self.brand} with {self.hp} HorsePower")

    def __str__(self) -> str:
        """sample dunder method to show details of the object"""
        return f"{self.brand} with {self.hp} Horsepower"

    def __add__(self, other: Self) -> str:  # Type annotation of Self for other object
        """sample dunder method to add  objects"""
        return f"{self.brand} & {other.brand}"  # if isinstance(other, Car):use if Self not imported

    def __repr__(self):
        """sample dunder method to add  objects"""
        return f"Make={self.brand} with hp={self.hp}"


volvo: Car = Car("volvo", 200)
volvo.drive()
volvo.get_info()

bmw: Car = Car("BMW", 250)
print(bmw) #invokes str
print(volvo + bmw)
print(repr(bmw))
print(bmw) #invokes str
print(str(bmw)) #same output as print(bmw)
