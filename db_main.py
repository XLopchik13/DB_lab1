from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self, id, name, surname, patronymic):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic


class Variant:
    def __init__(self, id, path):
        self.id = id
        self.path = path


students_list = []
for i in range(50):
    students_list.append([])
n = 1
i = 0
with open('names.txt', encoding="utf8") as f_names:
    for line in f_names:
        a = line.split()
        student = Student(n, a[0], a[1], a[2])
        #students_list[i].append(student.id, student.name, student.surname, student.patronymic)
        students_list[i].append(student.id)
        students_list[i].append(student.name)
        students_list[i].append(student.surname)
        students_list[i].append(student.patronymic)
        n += 1
        i += 1

with open('variants.txt', encoding="utf8") as f_variants:
    for line in f_variants:
        a = line.split()
        variant = Variant(a[0], a[1])
        #print(variant.id, variant.path)

print(students_list)
root = Tk()
root.title("Teacher program")
root.geometry("800x400")
columns = ("id", "name", "surname", "patronymic")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("id", text="id")
tree.heading("name", text="name")
tree.heading("surname", text="surname")
tree.heading("patronymic", text="patronymic")
for person in students_list:
    tree.insert("", END, values=person)
root.mainloop()

f_names.close()
f_variants.close()
