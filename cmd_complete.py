num = int(input())
cmd_set = []

for x in range(0, num):
    cmd_set.append(input())

prefix = input()

cmd_match = []
for x in cmd_set:
    if x[:len(prefix)] == prefix:
        cmd_match.append(x)

cmd_match.sort()

for x in cmd_match:
    print(x)