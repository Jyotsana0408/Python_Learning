class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role

    def show_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Role: {self.role}")


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, role):
        emp = Employee(emp_id, name, role)
        self.employees.append(emp)
        print(f"Employee '{name}' added!")

    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Employee '{emp.name}' removed!")
                return
        print(f"Employee with ID {emp_id} not found.")

    def show_all(self):
        print("\n Employee List:")
        if not self.employees:
            print("No employees added yet.")
        for emp in self.employees:
            emp.show_details()


manager = EmployeeManager()

manager.add_employee(101, "Jyotsna", "QA Engineer")
manager.add_employee(102, "Amit", "Developer")

manager.show_all()

manager.delete_employee(102)

manager.show_all()

