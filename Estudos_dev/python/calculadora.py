operador = input("Digite qual operador deseja utilizar(adicao,subtracao,multiplicacao,divisao.")
primeironumero = int(input("Digite o primeiro numero."))
segundonumero = int(input("Digite o segundo numero."))

if operador == "adicao":
        print(primeironumero+segundonumero)
elif operador == "subtracao":
        print(primeironumero-segundonumero)
elif operador == "multiplicacao":
        print(primeironumero*segundonumero)
elif operador == "divisao":
    print(primeironumero/segundonumero)