


"""
primaryNumber = 1



for indice in range(1,11):
    number = indice
    soma = 2* number
    

    if number == 10:
        primaryNumber +=1



print(f"2x{indice} é igual a : {soma}")
"""

startThread = True
number = 1
antigoNumero = 0



def Somar():
    for indice in range(1,11):
        number2 = indice
        soma = number* number2
        print(f"{number}x{indice} é igual a : {soma}")

Somar();

while startThread:

    if number != antigoNumero:
        number += 1
        antigoNumero += 1
        Somar()

    if number > 19:
        startThread = False