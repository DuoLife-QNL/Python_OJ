n, a = map(int, input().split())

def recur_multi(exp, a):
    if exp == n + 1:
        return a ** exp
    else:
        return recur_multi(exp + 1, a) + a ** exp

print(recur_multi(0, a))
