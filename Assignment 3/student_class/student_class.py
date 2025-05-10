# This program creats a Student class and displays student information.

class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display(self):
        print("\n--- Student Details ---")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Admission Year:", self.admission_year)
        print("Level:", self.level)
        print("Section:", self.section)

# Input from user
sid = input("Enter Student ID: ")
sname = input("Enter Name: ")
saddress = input("Enter Address: ")
syear = input("Enter Admission Year: ")
slevel = input("Enter Level: ")
ssection = input("Enter Section: ")

# Create object and display details
Student1 = Student(sid, sname, saddress, syear, slevel, ssection)
Student1.display()