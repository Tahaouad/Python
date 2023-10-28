import tkinter as tk
from tkinter import ttk

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

def create_student(db):
    student_id = int(student_id_entry.get())
    name = name_entry.get()
    age = int(age_entry.get())
    db.create_student(student_id, name, age)
    result_label.config(text="Étudiant ajouté avec succès.")

def read_student(db):
    student_id = int(student_id_entry.get())
    result = db.read_student(student_id)
    result_label.config(text=result)

def update_student(db):
    student_id = int(student_id_entry.get())
    name = name_entry.get()
    age = int(age_entry.get())
    result = db.update_student(student_id, name, age)
    result_label.config(text=result)

def delete_student(db):
    student_id = int(student_id_entry.get())
    result = db.delete_student(student_id)
    result_label.config(text=result)

def show_all_students():
    students = db.students
    if not students:
        result_label.config(text="Aucun étudiant enregistré.")
    else:
        show_students_window = tk.Toplevel()
        show_students_window.title("Liste des Étudiants")

        tree = ttk.Treeview(show_students_window, columns=("ID", "Nom", "Âge"))
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Nom")
        tree.heading("#3", text="Âge")

        for student in students:
            tree.insert("", "end", values=(student.student_id, student.name, student.age))

        tree.pack()

def on_closing():
    window.destroy()

db = StudentDatabase()

window = tk.Tk()
window.title("Gestion des Étudiants")

student_id_label = tk.Label(window, text="ID de l'étudiant:")
student_id_label.pack()
student_id_entry = tk.Entry(window)
student_id_entry.pack()

name_label = tk.Label(window, text="Nom de l'étudiant:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Âge de l'étudiant:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

add_button = tk.Button(window, text="Ajouter Étudiant", command=lambda: create_student(db))
read_button = tk.Button(window, text="Lire Étudiant", command=lambda: read_student(db))
update_button = tk.Button(window, text="Mettre à Jour Étudiant", command=lambda: update_student(db))
delete_button = tk.Button(window, text="Supprimer Étudiant", command=lambda: delete_student(db))
show_all_button = tk.Button(window, text="Afficher tous les étudiants", command=show_all_students)

add_button.pack()
read_button.pack()
update_button.pack()
delete_button.pack()
show_all_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
