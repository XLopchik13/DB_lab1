import random


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
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    print("table:", selected)
    print("id", " ".join(titles[ind]))
    for i in range(len(tbl)):
        print(tbl[i][0], " ".join(tbl[i][1][:end]))

    '''print("sorted table:")
    print("id", " ".join(titles[ind]))
    srt = sorted(table_list[ind].items(), key=lambda item: item[1])
    for i in range(len(srt)):
        print(srt[i][0], " ".join(srt[i][1][:end]))'''


def edit_line(cmd, table_names, cur_table, table_list):
    if len(cmd) != 2:
        print("incorrect input")
        return
    ind = table_names.index(cur_table)
    tbl = sorted(table_list[ind].items(), key=lambda item: item[0])
    for i in range(len(tbl)):
        if cmd[1] == str(tbl[i][0]):
            table_list[ind][int(cmd[1])] = cmd[2:]
            return
    print("selected non-existent line")


def delete_line(cmd, table_names, cur_table, table_list):
    if len(cmd) != 2:
        print("incorrect input")
        return
    ind1 = table_names.index(cur_table)
    ind2 = int(cmd[1])
    if ind2 in table_list[ind1]:
        del table_list[ind1][ind2]
        print("line with id:", cmd[1], "deleted")
    else:
        print("selected non-existent line")


def print_line(cmd, table_names, cur_table, table_list, titles):
    if len(cmd) != 2:
        print("incorrect input")
        return

    ind1 = table_names.index(cur_table)
    ind2 = int(cmd[1])
    end = len(titles[ind1])
    tbl = sorted(table_list[ind1].items(), key=lambda item: item[0])

    if ind2 in table_list[ind1]:
        print(ind2, " ".join(tbl[ind2-1][1][:end]))
    else:
        print("selected non-existent line")


def gen_table(cmd, table_names, table_list, generated_table):
    if len(cmd) != 3:
        print("incorrect input")
        return
    if cmd[1] not in table_names or cmd[2] not in table_names:
        print("incorrect tables selected")
        return

    ind_stud = table_names.index(cmd[1])
    ind_var = table_names.index(cmd[2])
    t_len = len(table_list[ind_stud])
    tbl = sorted(table_list[ind_stud].items(), key=lambda item: item[0])

    r_variants = list(table_list[ind_var].keys())
    random.shuffle(r_variants)

    j = 0
    for i in range(t_len):
        if j < len(r_variants):
            generated_table[int(tbl[i][0])] = r_variants[j]
            j += 1
        else:
            j = 0
            generated_table[int(tbl[i][0])] = r_variants[j]

    print("\ntesting table")
    print("stud_id | var_id")
    print("----------------")
    for key, value in generated_table.items():
        print("  ", key, "   ", value)

    print("\nfull_name | variant | mark")
    print("--------------------------")
    for key, value in generated_table.items():
        print(" ".join(table_list[ind_stud][key]), table_list[ind_var][value][0], "no mark", sep=' | ')

