total_match = int(input())
result = []
x = 1

while x <= total_match:
    win, lose = map(int, input().split())
    result.append([win, lose])
    x += 1

score = 0
for x in result:
    if (x[0] == 3 and (x[1] == 0 or x[1] == 1)):
        score += 3
    elif x[0] == 3 and x[1] == 2:
        score += 2
    elif x[0] == 2 and x[1] == 3:
        score += 1
    else:
        pass

print(score)