ch = input()
num = int(input())

l = []
for x in range(0, num):
    s = input()
    if (s.count(ch.upper()) + s.count(ch.lower()) >= 3):
        l.insert(0, s)

for x in l:
    print(x)
