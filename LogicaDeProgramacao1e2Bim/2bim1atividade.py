from random import randint 
from time import sleep

roleta = randint(1,6)
municaolocal = randint(1,6)


if roleta == municaolocal:
    print("💀🎇🔫")
else:
    print("Não foi dessa vez!")
  

municaolocal = randint(1,6)


while True:
    print("Tentando 🔫")
    sleep(2)
    roleta = randint(1,6)
    
    if roleta == municaolocal:
      print("💀🎇🔫")
      break
    else:
        print("Não foi dessa vez!")
