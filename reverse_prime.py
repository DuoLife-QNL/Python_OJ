import numpy as np
import math

def reverse(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result

def is_reverse(n):
    if n == reverse(n):
        return True
    else:
        return False

def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

a, b = map(int, input().split())

for x in range(a, b + 1):
    if is_reverse(x) and is_prime(x):
        print(x)