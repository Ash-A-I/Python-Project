"""
This is the entry point of the application. It uses a loop to interact with
the user, allowing them to add new students to the record, view students in the
record, update student marks and delete student record.
"""

from student_management import StudentManagement
def main():
    system = StudentManagement()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        ch = input("Enter Your Choice (1-5): ")
        try:
            if ch == "1":
                name = input("Enter Student Name: ")
                rollno = input("Enter Student RollNo: ")
                marks = float(input("Enter Student Marks: "))
                system.add_student(name, rollno, marks)

            elif ch == "2":
                system.view_students()

            elif ch == "3":
                rollno = input("Enter Student RollNo to Update Marks: ")
                marks = float(input("Enter New Marks: "))
                system.update_marks(rollno, marks)

            elif ch == "4":
                rollno = input("Enter Student RollNo to Delete: ")
                system.delete_student(rollno)

            elif ch == "5":
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid Choice. Please Select Between (1-5).")

        except ValueError:
            print("Invalid Input. Please Enter a Valid RollNo for Marks.")
        except Exception as e:
            print(f"Error: {e}")

main()
