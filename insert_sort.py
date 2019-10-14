length = int(input())
l = list(map(int, input().split()))

# should put l[i] into the right position
def insertion(l, i):
    j = i - 1
    key = l[i]
    while j >= 0 and key < l[j]:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = key

def output(l):
    for x in range(0, length - 1):
        print(l[x], end = " ")
    print(l[length - 1])

for x in range(1, length):
    insertion(l, x)
    output(l)    