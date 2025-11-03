students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nAll Students:")
print(students)

topper = max(students, key=students.get)
print(f"\nTopper: {topper} with {students[topper]} marks ")
