print("-"*20)
print("SISTEMA DE TROCA DE SENHAS - PY")
print("-"*20)


matricula = input("Digite sua matricula: ")


if matricula.isdigit() is False or len(matricula) != 11:
    print("Digite apenas 11 digitos.")
else:
    senha = input("Digite sua nova senha")


print(senha)