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

def main():
    db = StudentDatabase()

    while True:
        print("\nMenu:")
        print("1. Ajouter un étudiant")
        print("2. Lire un étudiant")
        print("3. Mettre à jour un étudiant")
        print("4. Supprimer un étudiant")
        print("5. Quitter")
        
        choice = input("Choisissez une option (1/2/3/4/5): ")
        
        if choice == "1":
            student_id = int(input("Entrez l'ID de l'étudiant : "))
            name = input("Entrez le nom de l'étudiant : ")
            age = int(input("Entrez l'âge de l'étudiant : "))
            db.create_student(student_id, name, age)
        elif choice == "2":
            student_id = int(input("Entrez l'ID de l'étudiant à lire : "))
            result = db.read_student(student_id)
            print(result)
        elif choice == "3":
            student_id = int(input("Entrez l'ID de l'étudiant à mettre à jour : "))
            name = input("Entrez le nouveau nom de l'étudiant : ")
            age = int(input("Entrez le nouvel âge de l'étudiant : "))
            result = db.update_student(student_id, name, age)
            print(result)
        elif choice == "4":
            student_id = int(input("Entrez l'ID de l'étudiant à supprimer : "))
            result = db.delete_student(student_id)
            print(result)
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Option non valide. Veuillez choisir une option valide.")

main()