# This program manages employee data using a class and write to CSV file.

import csv

class Employee:
    def __init__(self, empid, name, address, contact, spouse, children, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.children = children
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact, self.spouse, self.children, self.salary]
    
    def write_employees_to_file(employees, filename='employees.csv'):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Address", "Contact", "Spouse", "Children", "Salary"])
                for emp in employees:
                    writer.writerow(emp.to_list())
        except Exception as e:
            print("Error writing to file:", e)

def read_employees_from_file(filename='employees.scv'):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("File not found.")

employees = []
n = int(input("Enter number of employees: "))
for _ in range(n):
    try:
        empid = input("ID: ")
        name = input("Name: ")
        address = input("Address: ")
        contact = input("Contact: ")
        spouse = input("Spouse Name: ")
        children = int(input("Number of Children: "))
        salary = float(input("Salary: "))
        employees.append(Employee(empid, name, address, contact, spouse, children, salary))
    except Exception as e:
        print("Invalid input:", e)

write_employees_to_file(employees)
print("\nEmployee Records:")
read_employees_from_file()