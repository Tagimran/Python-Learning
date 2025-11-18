# Class Animal (parent) and Dog (child) – override method sound()

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark Bark"

# Class Shape with area() → subclass Circle, Rectangle implementing their own versions

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

# Private variable example (encapsulation)

class Bank:
    def __init__(self, balance):
        self.__balance = balance    # private variable

    def get_balance(self):
        return self.__balance

# Use super() in a child class to access parent method

class Person:
    def work(self):
        return "Working..."

class Programmer(Person):
    def work(self):
        parent_work = super().work()
        return parent_work + " and coding"

# Demonstrate polymorphism with multiple classes having same method name
class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

def make_sound(obj):
    return obj.sound()

if __name__ == "__main__":
    # Testing all parts

    # 1
    d = Dog()
    print(d.sound())

    # 2
    c = Circle(5)
    r = Rectangle(4, 6)
    print(c.area())
    print(r.area())

    # 3
    b = Bank(5000)
    print(b.get_balance())

    # 4
    p = Programmer()
    print(p.work())

    # 5
    print(make_sound(Cat()))
    print(make_sound(Cow()))
