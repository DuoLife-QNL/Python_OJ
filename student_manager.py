instr_num = int(input())

x = 0
instr = []
while x < instr_num:
    instr.append(input())
    x += 1

student_list = {}

class Student(object):
    def __init__(self, named, Mathd, Englishd, Pythond):
        self.name = named
        self.Math = Mathd
        self.English = Englishd
        self.Python = Pythond


class Student_Manager(object):
    def add_info(self, id, name, Math, English, Python):
        if id in student_list:
            print("Students already exist")
        else:
            student_list[id] = Student(name, Math, English, Python)
            print("Add success")

    def del_info(self, id):
        if id in student_list:
            student_list.pop(id)
            print("Delete success")
        else:
            print("Students do not exist")

    def update_info(self, id, Math, English, Python):
        if id in student_list:
            student_list[id].Math = Math
            student_list[id].English = English
            student_list[id].Python = Python
            print("Update success")
        else:
            print("Students do not exist")

    def display_grade(self, id):
        if id in student_list:
            name = student_list[id].name
            Math = student_list[id].Math
            English = student_list[id].English
            Python = student_list[id].Python
            print("Student ID:{}\nName:{}\nAverage Score:{:.1f}".format(id, name, (Math + English + Python)/3))
        else:
            print("Students do not exist")

manager = Student_Manager()

for x in instr:
    opr = x.split()
    if opr[0] == '1':
        manager.add_info(opr[1], opr[2], int(opr[3]), int(opr[4]), int(opr[5]))
    elif opr[0] == '2':
        manager.del_info(opr[1])
    elif opr[0] == '3':
        manager.update_info(opr[1], int(opr[2]), int(opr[3]), int(opr[4]))
    elif opr[0] == '4':
        manager.display_grade(opr[1])
