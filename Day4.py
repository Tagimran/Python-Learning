import utils  # importing your custom module

# Function to print your name 3 times

def print_name():
    name = input("Enter your name: ")
    for i in range(3):
        print(name)

# Function to add 3 numbers and return total

def add_three_numbers(a, b, c):
    total = a + b + c
    return total

# Function to check even or odd

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Function to calculate factorial

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Test the functions
if __name__ == "__main__":
    print_name()
    print("Sum:", add_three_numbers(5, 10, 15))
    check_even_odd(12)
    print("Factorial:", factorial(6))

# Create utils.py module with 2 math functions → import in day4.py

print("Square of 4:", utils.square(4))
print("Cube of 3:", utils.cube(3))
