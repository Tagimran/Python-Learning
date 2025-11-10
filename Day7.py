# Q1) Class Person with attributes name, age → method to display details
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Q2) Class Circle with method to find area and circumference
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Q3) Class Calculator with add, sub, mul, div methods
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


# Q4) Class Car with brand, model, year → display method
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Q5) Class Student → store marks in list → method to calculate average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


if __name__ == "__main__":
    print("=== Person Example ===")
    p1 = Person("Imran", 21)
    p1.display()

    print("\n=== Circle Example ===")
    c1 = Circle(5)
    print("Area:", c1.area())
    print("Circumference:", c1.circumference())

    print("\n=== Calculator Example ===")
    calc = Calculator()
    print("Add:", calc.add(10, 5))
    print("Sub:", calc.sub(10, 5))
    print("Mul:", calc.mul(10, 5))
    print("Div:", calc.div(10, 5))

    print("\n=== Car Example ===")
    car1 = Car("Toyota", "Fortuner", 2023)
    car1.display()

    print("\n=== Student Example ===")
    s1 = Student("Imran", [85, 90, 78, 92, 88])
    print("Average Marks:", s1.average())
