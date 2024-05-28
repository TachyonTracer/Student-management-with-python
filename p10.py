class Student:
    def __init__(self, name, email, phone, roll, id):
        self.name = name
        self.email = email
        self.phone = phone
        self.roll = roll
        self.id = id

    def print_student_details(self):
        print(f"{'Roll No.' : <3}{'Name' : ^10}{'Email' : ^22}{'    Phone' : ^12}{'   ID' : >14}")
        print(f"{self.roll : <3}{self.name : ^20}{self.email : ^10}{self.phone : ^22}{self.id : >10}")

students = {}

def add_student():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    roll = input("Enter Roll Number: ")
    id = input("Enter ID: ")
    students[roll] = Student(name, email, phone, roll, id)
    print("---------------------- Student Created ------------------------")
    students[roll].print_student_details()

def edit_student():
    roll = input("Enter the Roll Number of the student to edit: ")
    if roll in students:
        print("Current details:")
        students[roll].print_student_details()
        name = input("Enter new Name (leave blank to keep current): ")
        email = input("Enter new Email (leave blank to keep current): ")
        phone = input("Enter new Phone Number (leave blank to keep current): ")
        id = input("Enter new ID (leave blank to keep current): ")
        if name:
            students[roll].name = name
        if email:
            students[roll].email = email
        if phone:
            students[roll].phone = phone
        if id:
            students[roll].id = id
        print("--------------------- Student Updated ---------------------")
        students[roll].print_student_details()
    else:
        print("Student not found.")

def view_student():
    roll = input("Enter the Roll Number of the student to view: ")
    if roll in students:
        students[roll].print_student_details()
    else:
        print("Student not found.")

def view_all_students():
    print("========================== Student Data =============================")
    for roll, student in students.items():
        print("-----------------------------------------------------------------------")
        
        student.print_student_details()
def delete_student():
    roll = input("Enter the Roll Number of the student to delete: ")
    if roll in students:
        ch=input("Are you Sure : ")
        if ch == "y":
            del students[roll]
            print("Student deleted.")
        else:
            student_dashboard()
    else:
        print("Student not found.")
def student_dashboard():
    while True:
        print("=================== Welcome to the Dashboard =========================")
        print("1. Add a new student", "2. Edit a student", "3. Delete a student", "4. View a student", "5. View all students","6. Exit", sep="\n")
        ch = input("Enter Your Choice: ")
        if ch == "1":
            add_student()
        elif ch == "2":
            edit_student()
        elif ch == "3":
            delete_student()
            pass
        elif ch == "4":
            view_student()
        elif ch == "5":
            view_all_students()
        elif ch == "6":
            print("/==('-')==/  Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


student_dashboard()
