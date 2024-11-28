import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def firstNPrime(n):
    x = []
    for i in range(n):
        if is_prime(i):
            x += [i]
    return x


def eratL(n):
    L = [True] * (n + 1)
    L[0] = L[1] = False
    i = 5
    while i * i <= n + 1:
        if L[i]:
            for j in range(i * i, n + 1, i):
                L[j] = False
        i += 2
        if L[i]:
            for j in range(i * i, n + 1, i):
                L[j] = False
        i += 4
    Prim = [2, 3]
    for i in range(5, len(L) - 2, 6):
        if L[i]:
            Prim += [i]
        if L[i + 2]:
            Prim += [i + 2]
    return Prim


print(eratL(100))
