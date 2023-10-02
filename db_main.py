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

f_names.close()
f_variants.close()
