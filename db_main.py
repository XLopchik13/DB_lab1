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


print("          students")
print("id name    surname    patronymic")

n = 1
with open('names.txt', encoding="utf8") as f_names:
    for line in f_names:
        a = line.split()
        student = Student(n, a[0], a[1], a[2])
        print(student.id, student.name, student.surname, student.patronymic, sep='  ')
        n += 1

with open('variants.txt', encoding="utf8") as f_variants:
    for line in f_variants:
        a = line.split()
        variant = Variant(a[0], a[1])
        print(variant.id, variant.path)

root = Tk()
root.title("Teacher program")
root.geometry("800x400")
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
columns = ("id", "name", "surname", "patronymic")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("id", text="id")
tree.heading("name", text="name")
tree.heading("surname", text="surname")
tree.heading("patronymic", text="patronymic")
for person in people:
    tree.insert("", END, values=person)
root.mainloop()

f_names.close()
f_variants.close()
