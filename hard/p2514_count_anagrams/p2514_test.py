# test - understanding factorials

from math import factorial


def nPr(n, r):
    return int(factorial(n) / factorial(n - r))


print(factorial(0))
print(factorial(1))

print(nPr(7, 7))
print(nPr(3, 3))


