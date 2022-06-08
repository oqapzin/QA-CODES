valorInformado = float(input("Infome a quantide de dolares que deseja comprar: "))
valorReal = 4.72

if int(valorInformado) >= 0:
    valorConvetido = int(valorInformado) * valorReal
    print(f"Você vai gastar R${valorConvetido} para comprar {valorInformado}")