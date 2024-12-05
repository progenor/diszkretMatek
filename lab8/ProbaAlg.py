from random import randint, getrandbits
from base64 import b64encode, b64decode
from random import getrandbits
from random import randint

    
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

