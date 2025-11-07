# Topic: Exception Handling Examples

# Division Program with ZeroDivisionError Handling
print("---- Division Program ----")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Please enter valid numbers.")

# -----------------------------------------------------

# File Reading with FileNotFoundError Handling
print("\n---- File Read Program ----")
try:
    filename = input("Enter filename to read: ")
    with open(filename, 'r') as f:
        print("\nFile contents:\n", f.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")

# -----------------------------------------------------

# Custom Error Example (Age Check)
print("\n---- Custom Error Example ----")

class UnderAgeError(Exception):
    """Custom exception for underage users."""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise UnderAgeError("Access Denied! You must be 18 or older.")
    else:
        print("Access Granted")
except UnderAgeError as e:
    print(e)
except ValueError:
    print("Error: Please enter a valid number.")

# -----------------------------------------------------

#Try-Except-Finally Example
print("\n---- Try-Except-Finally Example ----")
try:
    num = int(input("Enter a number to square: "))
    print("Square is:", num ** 2)
except ValueError:
    print("Error: Invalid input.")
finally:
    print("Program block executed (finally).")

# -----------------------------------------------------

# Multiple Exceptions Together
print("\n---- Multiple Exceptions Example ----")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    lst = [10, 20, 30]
    index = int(input("Enter index to access (0-2): "))
    result = a / b
    print("Division Result:", result)
    print("List Value:", lst[index])
except (ZeroDivisionError, IndexError, ValueError) as e:
    print("Error occurred:", e)
finally:
    print("Multiple exception handling completed.")
