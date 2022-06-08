"""
numbers = [15,28,33]

maisVelho = 0
maisNovo = 0
maiorsoma = 0

for indice in range(0,4):
    maiorsoma = indice+1
    if numbers[indice] > numbers[maiorsoma]:
        print(numbers[indice])
"""


#Primeiro desafio 

"""numero = int(input("Digite o número: "))
if numero > 0:
    print("O número é maior do que zero, sendo assim positivo")
elif numero < 0:
    print("O número é menor do que zero, sendo assim negativo.")
else:
    print("O número é igual a zero.")
"""

#Segundo desafio

"""numero = int(input("Digite o número: "))
if numero == 0:
    print("O número é igual a zero.")
elif numero%2 == 0:
    print("O número é positivo.")
elif numero%2 == 1:
    print("O número é negativo.")
"""

#Terceiro desafio

"""numero = int(input("Digite o número: "))
if numero%3 == 0 and numero%5 == 0:
    print("divisível por 3 e 5")
elif numero%3 == 0:
    print("divisível por 3")
elif numero%5 == 0:
    print("divisível por 5")
"""





"""numbers = [44,47,22]

maisVelho = 0
maisNovo = 0

for indice in range(0,3):
    if numbers[indice] > numbers[(not indice+1 == 4)]:
        print(numbers[indice])
"""

primeiraidade = int(input("Digite a primeira idade: "))
segundaidade = int(input("Digite a segunda idade: "))
terceiraidade = int(input("Digite a terceira idade: "))


maioridade = 0
menoridade = 0

if segundaidade > terceiraidade:
    
    if primeiraidade > segundaidade and primeiraidade > terceiraidade:
        maioridade = primeiraidade 
        menoridade = terceiraidade
    else:
        maioridade = segundaidade 
        menoridade = terceiraidade
elif primeiraidade > terceiraidade and primeiraidade > segundaidade:
    maioridade = primeiraidade
    menoridade = segundaidade
else:
    maioridade = terceiraidade
    menoridade = primeiraidade


print(f"A maior idade é {maioridade}, e a menor idade é {menoridade}")