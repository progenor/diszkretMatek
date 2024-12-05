import socket               
import ProbaAlg
import random

BF_SIZE = 2048
host = 'localhost'
port = 12353

def keyServer(c):
      #p = 18952415480139660683
      #gen = 11041898282678223887
      p = 14333533999263997762309036457882954888756012061604018294438354422870408323639
      gen = 3084224261994970117278311615343465379127203005451339009062617885322268239459
      pList = ProbaAlg.nrToBase256(p)
      genList = ProbaAlg.nrToBase256(gen)
      
      a = random.randint(2, p - 1)
      A = pow(gen, a, p)
      aList = ProbaAlg.nrToBase256(A)
      #1
      mess = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', mess.decode())
      c.send(bytes(pList))

      #2
      mess = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', mess.decode())
      c.send(bytes(genList))

      #3
      mess = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', mess.decode())
      c.send(bytes(aList))

      #4
      mess = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', mess.decode())
      c.send('hello!'.encode())

      #5
      bList = c.recv(BF_SIZE)
      B = ProbaAlg.nrFromBase256(bList)
      
      K = pow(B, a, p)
      print ('K:', K)
      c.send('meghatároztam a közös mesterkulcsot!'.encode())

      #6
      data = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', data.decode())
      c.send('viszontlátásra!'.encode())

      #7
      mess = c.recv(BF_SIZE)
      print ('a klienstől kapott üzenet: ', mess.decode())

      return c

def mainS():
   c = None
   while True:
      x = input("""
            0- leállítás, szerver
            1- indítás, szerver
            2- mesterkulcs megállapodás
            """)
      if x == '0':
         if c != None:
               print ('leáll a szerver...')
               c.close()
         break
      if x == '1':
         if c != None:
            print ('a szerver már el van indítva!')
            continue
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         print ('várakozás (indítsd el a klienst)...')
         s.bind((host, port))        
         s.listen(5)
         c, addr = s.accept()     
         print ('a kapcsolat a következő címen jött létre: ', addr)
      if x == '2':
         if c == None:
            print ('előbb indítsd el a szervert!')
            continue
         c = keyServer(c)

mainS()
