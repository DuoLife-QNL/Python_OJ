num = int(input())

name_list = []

for x in range(0, num):
    s = input()
    name = s.split()
    name_list.append(name)

last_name = input()
match = []
for x in name_list:
    if (x[1] == last_name):
        match.append(x[0])

match.sort()

for x in match:
    print(x)