from random import randint 
from time import sleep

roleta = randint(1,6)
municaolocal = randint(1,6)


if roleta == municaolocal:
    print("ððð«")
else:
    print("NÃ£o foi dessa vez!")
  

municaolocal = randint(1,6)


while True:
    print("Tentando ð«")
    sleep(2)
    roleta = randint(1,6)
    
    if roleta == municaolocal:
      print("ððð«")
      break
    else:
        print("NÃ£o foi dessa vez!")
