a, b = map(int, input().split())

if a > b:
    print("The larger number is {}, the smaller number is {}.".format(a, b))
elif b > a:
    print("The larger number is {}, the smaller number is {}.".format(b, a))
elif a == b:
    print("The two numbers are equal.")