def new_table(titles, table_list, table_names, cmd):
    index = 0
    titles.append(cmd[2::])
    table_list.append({})
    table_names.append(cmd[1])
    print(titles, table_list, table_names)


def add_row(table_names, table_list, cur_table, cmd):
    ind = table_names.index(cur_table)
    table_list[ind][len(table_list[ind])+1] = cmd[1::]


def print_table(cmd, table_names, titles, table_list):
    selected = cmd[1]
    if selected not in table_names:
        print('table "', selected, '" does not exist', sep='')
        return
    ind = table_names.index(selected)
    print("table:", selected)

    print("id", " ".join(titles[ind]))
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        print(tbl[i][0], " ".join(tbl[i][1]))

    print()
    print("sorted table:")
    print("id", " ".join(titles[ind]))
    srt = sorted(table_list[ind].items(), key=lambda item: item[1])
    for i in range(len(srt)):
        print(srt[i][0], " ".join(srt[i][1]))


def edit_line(cmd, table_names, cur_table, table_list):
    ind = table_names.index(cur_table)
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        if cmd[1] == tbl[i][0]:

            return
    print("selected non-existent line")


def delete_line(cmd, table_names, cur_table, table_list):
    ind = table_names.index(cur_table)
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        if cmd[1] == tbl[i][0]:

            return
    print("selected non-existent line")
