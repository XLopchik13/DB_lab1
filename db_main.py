from tkinter import *
from tkinter import ttk
from functions import *

titles = []  # названия столбцов
table_list = []  # список таблиц
generated_table = {}
table_names = []  # названия таблиц
cur_table = ''

print("Добро пожаловать в систему оценивания студентов!", 'Чтобы увидеть команды, введите /help', sep='\n')
cmd = 0
while cmd != '/e':
    cmd = input().split()
    if cmd[0] == '/help':
        print("new table: /nt #table_name #surname-name-midname")
        print("select table: /st #table_name")
        print("add row: /add #surname-name-midname")
        print("print table: /pt #table_name")
        print("delete row: /dl #row_number")
        print("print row: /pr #row_number")
        print("edit cell: /edc #row #column #new_data")
        print("clear cell: /dc #row #column")
        print("exit: /e")
    elif cmd[0] == '/nt':
        new_table(titles, table_list, table_names, cmd)

    elif cmd[0] == '/st':
        if len(cmd) == 2 and cmd[1] in table_names:
            cur_table = cmd[1]
            print('selected "', cur_table, '"', sep='')
        else:
            print("wrong command")


    elif cmd[0] == '/add':
        if cur_table != '':
            add_row(table_names, table_list, cur_table, cmd)
        else:
            print("table not selected")

    elif cmd[0] == '/pt':
        if len(cmd) != 2:
            print("wrong command")
        else:
            print_table()

    elif cmd[0] == '/dl':
        if len(cmd) != 2:
            print("wrong command")
        else:
            pass

    elif cmd[0] == 'pr':
        if len(cmd) != 2:
            print("wrong command")
        else:
            pass

    elif cmd[0] == 'edc':
        if len(cmd) != 4:
            print("wrong command")
        else:
            pass

    elif cmd[0] == 'dc':
        if len(cmd) != 3:
            print("wrong command")
        else:
            pass

    elif cmd[0] == '/e':
        print("o kurwa")
        break

    else:
        print("wrong command")




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
root.mainloop()'''
