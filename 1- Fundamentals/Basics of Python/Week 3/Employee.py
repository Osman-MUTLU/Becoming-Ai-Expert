from Person import Person

class Employee(Person):
    def __init__(self, name, surname, phone, email,department,salary):
        self.department=department
        self.salary=salary
        super().__init__(name, surname, phone, email)
    def display(self):
        super().display()
        print("Department :",self.department)
        print("Salary :",self.salary)