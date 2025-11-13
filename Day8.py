# Class Animal (parent) and Dog (child) – override method sound()

# Class Shape with area() → subclass Circle, Rectangle implementing their own versions

# Private variable example (encapsulation)

# Use super() in a child class to access parent method

# Demonstrate polymorphism with multiple classes having same method name

class Bird:
    def fly(self):
        print("Most birds can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly!")

for bird in [Bird(), Penguin()]:
    bird.fly()
