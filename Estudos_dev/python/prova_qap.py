questaoa = str(input("Digite a opção da questão 01 (A,B,C,D): "))
questaob = str(input("Digite a opção da questão 02 (A,B,C,D): "))
questaoc = str(input("Digite a opção da questão 03 (A,B,C,D): "))
questaod = str(input("Digite a opção da questão 04 (A,B,C,D): "))
questaoe = str(input("Digite a opção da questão 05 (A,B,C,D): "))
questaof = str(input("Digite a opção da questão 06 (A,B,C,D): "))

prova_aluno = [questaoa,questaob,questaoc,questaod,questaoe,questaof]
prova_correcao = ("A","B","D","C","C","B")
soma = 0

for indice in range(5):
    if prova_correcao[indice] == prova_aluno[indice]:
        soma += 1
        print(f"O aluno acertou a questão {indice}, sua nota é de {soma}")
    else:
        print(f"O aluno errou a questão {indice}, a resposta que ele colocou foi {prova_aluno[indice]}, e a correta seria {prova_correcao[indice]}. Sua nota é de {soma}")