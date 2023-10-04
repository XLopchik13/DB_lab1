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


print("Добро пожаловать в систему оценивания студентов!", 'Чтобы увидеть команды введите /help', sep='\n')
cmd = 0
while cmd != '/e':
    cmd = input()
    if cmd == '/help':
        print("new table: /nt #table_name []")
        print("select table: /st #table_name")
        print("print table: /pt #table_name")
        print("add row: /add []")
        print("delete row: /dl #row_number")
        print("print row: /pr #row_number")
        print("edit cell: /edc #row #column [new data]")
        print("delete cell: /dc")
        print("exit: /e")
    elif cmd[0:4] == '/st ':
        print(cmd[4::])
    elif cmd == '/e':
        print("o kurwa")
    else:
        print("wrong command")


students_list = []
for i in range(50):
    students_list.append([])
variants_list = []
for i in range(10):
    variants_list.append([])

with open('names.txt', encoding="utf8") as f_names:
    n = 1
    i = 0
    for line in f_names:
        a = line.split()
        # student = Student(n, a[0], a[1], a[2])
        # students_list[i] = [student.id, student.name, student.surname, student.patronymic]
        students_list[i] = [n, a[0], a[1], a[2]]
        n += 1
        i += 1

with open('variants.txt', encoding="utf8") as f_variants:
    i = 0
    for line in f_variants:
        a = line.split()
        # variant = Variant(a[0], a[1])
        variants_list[i] = [a[0], a[1]]
        i += 1

'''root = Tk()
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
f_variants.close()'''
