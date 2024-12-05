from random import randint


def MillerRabin(nr, t=10):
    r, s = nr - 1, 0
    while r % 2 == 0:
        r = r // 2
        s += 1
    for i in range(t):
        x = randint(2, nr)
        temp = pow(x, r, nr)
        if temp == 1 or temp == -1:
            continue
        for j in range(0, s):
            temp = (temp * temp) % nr
            if temp == nr - 1:
                break
            if temp == -1:
                return False
        if temp != nr - 1:
            return False
    return True


print(MillerRabin(200))
