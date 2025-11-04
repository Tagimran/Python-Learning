def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

print("Select Operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice (1-4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(a,b))
elif choice == '2':
    print("Result:", sub(a,b))
elif choice == '3':
    print("Result:", mul(a,b))
elif choice == '4':
    print("Result:", div(a,b))
else:
    print("Invalid Input")
