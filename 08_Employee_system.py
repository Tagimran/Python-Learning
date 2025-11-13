class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ₹{self.salary}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language
    
    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size
    
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

# Demonstrate polymorphism
employees = [
    Developer("Imran", 101, 80000, "Python"),
    Manager("Sara", 102, 100000, 5)
]

for emp in employees:
    emp.show_details()
    print()
