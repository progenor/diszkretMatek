from random import randint, getrandbits
from base64 import b64encode, b64decode
from random import getrandbits
from random import randint
from sympy import isprime
import math
    
def nrFromBase256(L):
    nr = 0
    for elem in L:
        nr = (nr << 8) + elem
    return nr

def nrToBase256(nr):
    L = []
    while nr > 0:
        L = [nr & 255] + L
        nr = nr >> 8 # nr = nr // 256
    return L
    
def nrToBase256_(nr, k): #k - bit
    k = k // 8 + 1
    L = nr.to_bytes(k, byteorder = 'big')
    return L

def nrFromBase256_(L):
    nr = int.from_bytes(L, byteorder = 'big')
    return nr

def int_toBase64(n):
    return b64encode(n.to_bytes(n.bit_length(), byteorder='big')).decode()

def RSA_keyWrite(k=1024, filename1 = 'lab8/RSA_publicKey.txt', filename2 = 'lab8/RSA_privateKey.txt'):
    p, q, n, e, d = RSA_keygen(k)
    with open(filename1, 'w') as f:
        f.write(int_toBase64(e) + '\n')
        f.write(int_toBase64(n) + '\n')
    with open(filename2, 'w') as f:
        f.write(int_toBase64(d) + '\n')
        f.write(int_toBase64(p) + '\n')
        f.write(int_toBase64(q) + '\n')

def int_fromBase64(s):
    return int.from_bytes(b64decode(s.encode()), byteorder='big')


def RSA_publicKeyRead(filename = 'lab8/RSA_publicKey.txt'):
    with open(filename, 'r') as f:
        n = int_fromBase64(f.readline().strip())
        e = int_fromBase64(f.readline().strip())
    return (e, n)

def RSA_privateKeyRead(filename = 'lab8/RSA_privateKey.txt'):
    with open(filename, 'r') as f:
        d= int_fromBase64(f.readline().strip())
        p = int_fromBase64(f.readline().strip())
        q = int_fromBase64(f.readline().strip())
        
    return (d, p, q)

def primeGen(n=1024):
    while True:
        p = getrandbits(n)
        if p & 1 == 0:
            p += 1
        if isprime(p):
            return p

def RSA_keygen(n=1024):
    p = primeGen(n)
    q = primeGen(n)
    
    n = p * q

    e = 3
    while True:
        if math.gcd(e, (p-1)*(q-1)) == 1:
            break
        e += 2
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return p, q, n, e, d

def RSA_encrypt(filename = 'lab8/RSA_publicKey.txt'):
    e, n = RSA_publicKeyRead()
    
    strk = input('Message:')
    k = int.from_bytes(strk.encode(), byteorder='big')
    # k = int(input('k = '))
    ck = pow(k, e, n)

    ckBytes = ck.to_bytes(length=ck.bit_length(), byteorder='big')
    return ckBytes, len(strk)    

def RSA_decrypt(ckBytes, cklen, filename = 'lab8/RSA_privateKey.txt'):
    d, p, q = RSA_privateKeyRead()
    n = p * q
    ck = int.from_bytes(ckBytes, byteorder='big')
    k = pow(ck, d, n)
    
    message = k.to_bytes(cklen, byteorder='big')
    print("visszafejtett ertek", message.hex())

def RSA_main():
    RSA_keyWrite()
    ckBytes, ckLen = RSA_encrypt()
    print("titkositott ertek", ckBytes)
    RSA_decrypt(ckBytes, ckLen)


def RSA_testNumbers():
    RSA_keyWrite(64)
    e, n = RSA_publicKeyRead()
    d, p, q = RSA_privateKeyRead()
    print('e =', e)
    print('n =', n)
    print('d =', d)
    print('p =', p)
    print('q =', q)
    
    strk = input('Message:')
    k = int.from_bytes(strk.encode(), byteorder='big')
    
    # k = int(input('k = '))
    ck = pow(k, e, n)

    ckBytes = ck.to_bytes(ck.bit_length(), byteorder='big')
    print("titkositott ertek", ck)
    n = p *q
    k1 = pow(ck, d,n)
    print("visszafejtett ertek", k1)



RSA_main()