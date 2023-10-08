def new_table(titles, table_list, table_names, cmd):
    index = 0
    titles.append(cmd[2::])
    table_list.append({})
    table_names.append(cmd[1])
    print(titles, table_list, table_names)


def add_row(table_names, table_list, cur_table, cmd):
    ind = table_names.index(cur_table)
    table_list[ind][len(table_list[ind])+1] = cmd[1::]
    print(table_list)


def print_table():
    pass
