# Even / Odd Checker

a = 11
if (a%2!=0):
    print(f"{a} is Odd Number")
else:
    print(f"{a} is Even Number")

# Grade Calculator

Python = 84
Java = 67
C_lan = 76
Cpp = 99
DBMS = 58

Marks = Python + Java + C_lan + Cpp + DBMS
avg = Marks / 5

if(avg >= 91 and avg <= 100):
    print("Your Grade is A1")
elif(avg >= 81 and avg < 91):
    print("Your Grade is A2")
elif(avg >= 71 and avg < 81):
    print("Your Grade is B1")
elif(avg >= 61 and avg < 71):
    print("Your Grade is B2")
elif(avg >= 51 and avg < 61):
    print("Your Grade is C1")
elif(avg >= 41 and avg < 51):
    print("Your Grade is C2")
elif(avg >= 33 and avg < 41):
    print("Your Grade is D")
elif(avg >= 21 and avg < 33):
    print("Your Grade is E1")
elif(Avg >= 0 and avg < 21):
    print("Your Grade is E2")
else:
    print("Invalid Input!")
# Largest of 3 numbers

n1= 10
n2= 3
n3= 21
if(n1>n2 and n1>n3):
    print(f"{n1} is Greater than {n2},{n3}")
elif(n2>n3):
    print(f"{n2} is Greater than {n1},{n3}")
else:
    print(f"{n3} is Greater than {n1},{n2}")

# Print 1 to 10 using for

for i in range(10):
    print(i + 1) 
# Sum of first n natural numbers
N= 10
total= 0
for i in range(1,N+1):
    total += i
print(f"Sum of first n natural numbers : {total}")

# Multiplication Table

for i in range(10):
    print(f"5 x {i} = {5*(i + 1)}") 
