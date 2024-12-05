import socket               
import random
import ProbaAlg

BF_SIZE = 2048
host = 'localhost'
port = 12353


def keyKliens(s):
    #1
    s.send('hello!'.encode())
    pList = s.recv(BF_SIZE)
    p = ProbaAlg.nrFromBase256(pList)
    
    #2
    s.send('megkaptam a p értékeket!'.encode())
    genList = s.recv(BF_SIZE)
    gen = ProbaAlg.nrFromBase256(genList)

    #3
    s.send('megkaptam a gen értékeket!'.encode())
    aList = s.recv(BF_SIZE)

    #4
    s.send('megkaptam az A értékét!'.encode())
    A = ProbaAlg.nrFromBase256(aList)
    
    b = random.randint(2, p - 1)
    B = pow(gen, b, p)
    bList = ProbaAlg.nrToBase256(B)
    
    mess = s.recv(BF_SIZE)
    print ('a szervertől kapott üzenet: ', mess.decode())

    #5
    s.send(bytes(bList))
    K = pow(A, b, p)
    print ('K: ', K)
    
    mess = s.recv(BF_SIZE)
    print ('a szervertől kapott üzenet: ', mess.decode())

    #6
    s.send('meghatároztam a közös mesterkulcsot!'.encode())

    mess = s.recv(BF_SIZE)
    print ('a szervertől kapott üzenet: ', mess.decode())

    #7
    s.send('viszontlátásra!'.encode())
    return s

def mainK():
   s = None
   while True:
      x = input("""
        0- leállítás, kliens
        1- indítás, kliens
        2- mesterkulcs megállapodás
        """)
      if x == '0':
         if s != None:
             print ('leáll a kliens...')
             s.close()
         break
      if x == '1':
         if s != None:
            print ('a kliens már el van indítva!')
            continue
         try:
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             s.connect((host, port))
             print ('letrejött a kapcsolat!')
         except:
             s = None
             print ('előbb indítsd el a szervert!')
      if x == '2':
         if s == None:
            print ('előbb indítsd el a klienst!')
            continue
         s = keyKliens(s)

mainK()
