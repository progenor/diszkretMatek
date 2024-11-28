from random import choice


def feladat():
    L = "abcdefghijklmnopqrstuvxyz"
    c = choice(L)
    print("a betu: ", c)

    L = ["iphone", "samsung", "huawei", "nokia"]
    c = choice(L)
    print("a telefon: ", c)


feladat()
