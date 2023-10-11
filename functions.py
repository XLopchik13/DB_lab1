def new_table(titles, table_list, table_names, cmd):
    if cmd[1] in table_names:
        print("table with the same name already exists")
        return
    titles.append(cmd[2::])
    table_list.append({})
    table_names.append(cmd[1])
    cur_table = cmd[1]
    print('created and selected table "', cur_table, '"', sep='')
    return cur_table


def add_row(table_names, table_list, cur_table, cmd):
    ind = table_names.index(cur_table)
    table_list[ind][len(table_list[ind])+1] = cmd[1::]


def print_table(cmd, table_names, titles, table_list):
    selected = cmd[1]
    if selected not in table_names:
        print('table "', selected, '" does not exist', sep='')
        return
    ind = table_names.index(selected)
    end = len(titles[ind])
    print("table:", selected)

    print("id", " ".join(titles[ind]))
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        print(tbl[i][0], " ".join(tbl[i][1][:end]))

    '''print("sorted table:")
    print("id", " ".join(titles[ind]))
    srt = sorted(table_list[ind].items(), key=lambda item: item[1])
    for i in range(len(srt)):
        print(srt[i][0], " ".join(srt[i][1][:end]))'''


def edit_line(cmd, table_names, cur_table, table_list):
    if len(cmd) < 2:
        print("selected non-existent line")
        return
    ind = table_names.index(cur_table)
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        if cmd[1] == str(tbl[i][0]):
            table_list[ind][int(cmd[1])] = cmd[2:]
            return
    print("selected non-existent line")


def delete_line(cmd, table_names, cur_table, table_list):
    if len(cmd) < 2:
        print("selected non-existent line")
        return
    ind = table_names.index(cur_table)
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        if cmd[1] == str(tbl[i][0]):
            deleted = table_list[ind][int(cmd[1])].pop()
            print(deleted, "- deleted")
            return
    print("selected non-existent line")
