"""
This Module defines student and Student Management Classes with student class
having attributes for name, rollno and marks of the student.

Student Management Class allows adding student, viewing students in the record,
updating student marks and deleting student records.
"""
#Class to represent a student.
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return f"Name:{self.name}, RollNo:{self.rollno}, Marks:{self.marks}"

#Class to manage students.
class StudentManagement:
    def __init__(self):
        self.students = []  # List to store students

    def add_student(self, name, rollno, marks):
        # Check if the student already exists
        for student in self.students:
            if student.rollno == rollno:
                print(f"Student with RollNo {rollno} already exists.")
                return
        # If student does not exist, add the new student
        new_student = Student(name, rollno, marks)
        self.students.append(new_student)
        print(f"Student {name} has been added.")

    def view_students(self):
        if len(self.students) == 0:
            print("No students available.")
        else:
            print("Current students:")
            for student in self.students:
                print(student)

    def update_marks(self, rollno, marks):
        for student in self.students:
            if student.rollno == rollno:
                student.marks = marks
                print(f"Marks for {student.name} updated to {marks}.")
                return
        print(f"Student with RollNo {rollno} not found.")

    def delete_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                print(f"Student {student.name} deleted.")
                return
        print(f"Student with RollNo {rollno} not found.")
