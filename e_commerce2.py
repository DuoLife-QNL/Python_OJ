n = int(input())

l = []
for x in range(0, n):
    l.append(input())

def abbr(name):
    name_l = list(name)
    x = 0
    while x < len(name_l):
        if name_l[x] <= 'z' and name_l[x] >= 'a':
            del name_l[x]
            x -= 1
        x += 1
    return "".join(name_l)

l.sort(key = abbr)

for x in l:
    print(x)