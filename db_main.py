from tkinter import *
from tkinter import ttk
from functions import *


titles = []
table_list = []
generated_table = {}
table_names = []
cur_table = ''

print("STUDENT ASSESSMENT SYSTEM", 'To see the commands, enter /help', sep='\n')
cmd = 0
while True:
    cmd = input().split()
    if len(cmd) == 0:
        continue

    elif cmd[0] == '/help':
        print("new table: /nt #table_name #surname-name-midname")
        print("select table: /st #table_name")
        print("add row: /add #surname-name-midname")
        print("print table: /pt #table_name")
        print("edit line: /el #line_id #surname-name-midname")
        print("delete line: /dl #line_id")
        print("print line: /pl #line_id")
        print("generate table: /gen #students_table #variants_table")
        print("add rows from file: /aff #filename")
        print("exit: /e")

    elif cmd[0] == '/nt':
        cur_table = new_table(titles, table_list, table_names, cmd)

    elif cmd[0] == '/st':
        if len(cmd) == 2 and cmd[1] in table_names:
            cur_table = cmd[1]
            print('selected table "', cur_table, '"', sep='')
        else:
            print("wrong command")

    elif cmd[0] == '/add':
        if cur_table != '':
            add_row(table_names, table_list, cur_table, cmd)
        else:
            print("table not selected")

    elif cmd[0] == '/pt':
        print_table(cmd, table_names, titles, table_list)

    elif cmd[0] == '/el':
        edit_line(cmd, table_names, cur_table, table_list)

    elif cmd[0] == '/dl':
        delete_line(cmd, table_names, cur_table, table_list)

    elif cmd[0] == '/pl':
        print_line(cmd, table_names, cur_table, table_list, titles)

    elif cmd[0] == '/gen':
        gen_table(cmd, table_names, table_list, generated_table)

    elif cmd[0] == '/aff':
        add_from_file(table_names, table_list, cur_table, cmd)

    elif cmd[0] == '/e' and len(cmd) == 1:
        print("-----EXIT-----")
        break

    else:
        print("wrong command")
