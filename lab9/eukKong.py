# magyarazat
# 3*x =1 mod 13
# if (3, 13)=1 --realtive primek
# a*x=1 mod p , p prim
# a in {0, ... p-1}

# what if insted of p is an n wich is n=p*q

# it can be solved with eukledian algorithm
import math


def modInv(a, b):
    x0, x1, b1 = 1, 0, b
    while True:
        q = a//b
        r = a%b # igy is ki lehet szamitani r= a - q*b
        if r == 0:
            if b != 1:
                return -1;
            else:
                return x1%b1; # normalisan -4 az eredmen 3,13 ra mertakkor 9 kell nekunk ami 13 - 9           
        a = b
        b = r
        x = x0 - q*x1
        x0=x1
        x1=x

# print(modInv(3, 13)) # 9  

def fel1():
    with open("szamok.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            a, m = map(int, line.split())
            # if isRelativePrime(a, p):
            #     print(f"{a} és {p} relatív prímek")
            # else:
            #     print(f"{a} és {p} nem relatív prímek")                        
            if math.gcd(a, m)==1:
                k=modInv(a, m)
                print(f"Van megoldas: {k}, k*a%m = 1 : {k*a%m}")
            else:
                pass



def modLim(a, b):
    x0, x1, b1 = 1, 0, b
    while True:
        q = a//b
        r = a%b # igy is ki lehet szamitani r= a - q*b
        if r == 0:
            return b, x1
        a = b
        b = r
        x = x0 - q*x1
        x0=x1
        x1=x


def printFile( m, x0, d):
    with open(f"generatedFiles/file{d}.txt", "w")as f:
        for i in range(d):
            x=x0+i*(m//d)
            print(x, file = f)
            
def printConsole( m, x0, d):
    for i in range(d):
        x=x0+i*(m//d)
        print(x)
            
def fel2():
    with open("szamokH.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            a,m,b = map(int, line.split())
            d,x = modLim(a,m)
            if b%d==0:
               x0=x*(b//d)
               print(f"Van megoldas: {x0}, {x0*a%m}={b} mod {m} ; megoldas szama {d}") 
               if d>10:
                    printFile( m, x0, d)
               elif d>1:
                    printConsole( m, x0, d)
               else:
                   print("Nincs megoldas")

# Az szamokHP allomanyban számpárok vannak: a, m egész számok. Olvassuk ki rendre ezeket a számokat, és ha az m prímszám, a kis Fermat tétel segítségével, minden számpárra, oldjuk meg az alábbi lineáris kongruenciát: a·x = 1 mod m, azaz határozzuk meg az a szám inverzét mod m szerint.
def smallFermat(a, m):
    return pow(a, m-2, m)

def fel3():
    with open("szamokHP.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            a, m,b = map(int, line.split())
            if math.gcd(a, m)==1:
                k=smallFermat(a, m)
                print(f"Van megoldas: {k}, k*a%m = 1 : {k*a%m}")
            else:
                print("Nincs megoldas")             

# Az szamokP állományban számhármasok vannak: a, m, b egész számok. Olvassuk ki rendre ezeket a számokat és ha az m prímszám, akkor a kis Fermat tétel segítségével, minden számhármasra, oldjuk meg az alábbi lineáris kongruenciát: a·x = b mod m.

def fel4():
    with open("szamokP.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            a, m, b = map(int, line.split())
            if math.gcd(a, m) == 1:
                k = smallFermat(a, m)
                x = (k * b) % m
                print(f"Van megoldas: x = {x}, a*x % m = {a * x % m}")
            else:
                print("Nincs megoldas")

if __name__ == "__main__":
    # fel1()
    # fel2()
    # fel3()
    fel4()
    pass