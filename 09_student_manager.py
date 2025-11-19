class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")


class StudentManager:
    FILE = "students.txt"

    def add_student(self):
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        marks = input("Enter marks: ")

        with open(self.FILE, "a") as f:
            f.write(f"{name},{roll},{marks}\n")

        print("Student added!")

    def view_students(self):
        with open(self.FILE, "r") as f:
            print("\nAll Students:")
            for line in f:
                name, roll, marks = line.strip().split(",")
                s = Student(name, roll, marks)
                s.display()

    def search_student(self):
        key = input("Enter name to search: ")
        found = False

        with open(self.FILE, "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                if name.lower() == key.lower():
                    print("\nStudent Found:")
                    Student(name, roll, marks).display()
                    found = True
                    break
        if not found:
            print("Student not found.")

    def delete_student(self):
        key = input("Enter name to delete: ")

        lines = []
        with open(self.FILE, "r") as f:
            lines = f.readlines()

        with open(self.FILE, "w") as f:
            deleted = False
            for line in lines:
                name, roll, marks = line.strip().split(",")
                if name.lower() != key.lower():
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Student deleted successfully.")
        else:
            print("Student not found.")


manager = StudentManager()

while True:
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1': manager.add_student()
    elif choice == '2': manager.view_students()
    elif choice == '3': manager.search_student()
    elif choice == '4': manager.delete_student()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid input.")
