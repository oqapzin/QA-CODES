import random 
dadoiniciado = False
numerodado = 0

if not dadoiniciado:
    numerodado = random.randint(3, 9)
    print(f"Seu dado é {numerodado}")
    dadoiniciado = True 
    jogarnovamente = input('Você gostaria de jogar o dado?')
    if dadoiniciado and type(jogarnovamente) == str:
        print("dentro")
    else:
        jogarnovamente = input('Você gostaria de jogar o dado?')
