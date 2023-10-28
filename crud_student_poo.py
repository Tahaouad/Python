class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

class StudentDatabase:
    def __init__(self):
        self.students = []

    def create_student(self, student_id, name, age):
        student = Student(student_id, name, age)
        self.students.append(student)

    def read_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return f"Student ID: {student.student_id}, Name: {student.name}, Age: {student.age}"
        return "Student not found."

    def update_student(self, student_id, name, age):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                return "Student updated successfully."
        return "Student not found."

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return "Student deleted successfully."
        return "Student not found."

db = StudentDatabase()

db.create_student(1, "OUAD", 20)
db.create_student(2, "DOUIRY", 22)

print(db.read_student(1))
print(db.read_student(3))  

db.update_student(1, "Taha", 21)
print(db.read_student(1))  
db.delete_student(2)
print(db.read_student(2))  
