#CONVERSOR SIMPLES

"""
primaryNumber = int(input("Informe o numero: "))

if primaryNumber > 0:
    celsiusConvertor = (primaryNumber-32)*(5/9)
    print(f"{primaryNumber}ºF são exatamente {celsiusConvertor}° celsius")
else:
    print("Esse conversor não aceita numeros nulos ou abaixo de 1.")
"""

#CONVERSOR MALUCO

conversorType = input("Qual conversão você deseja utilizar? (CF = Celsius for Fahrenheit | FC = Fahrenheit for Celsius | KC = Kelvin for Celsius | KF = Kelvin for Fahrenheit : ")
primaryNumber = int(input("Informe o número: "))


if primaryNumber > 0:
    
    if conversorType == "FC":
        celsiusConvertor = (primaryNumber-32)*(5/9)
        print(f"{primaryNumber}ºF são exatamente {celsiusConvertor}° celsius.")
    elif conversorType == "CF":
        FahrenheitConvertor = (primaryNumber*9/5)+32
        print(f"{primaryNumber}ºC são exatamente {FahrenheitConvertor}° fahrenheit.")
    elif conversorType == "KC":
        KelvinConvertor = (primaryNumber-273.15)
        print(f"{primaryNumber}K são exatamente {KelvinConvertor}° celsius.")
    elif conversorType == "KF":
        KelvinConvertor2 = (primaryNumber-273.15)* 9/5 + 32
        print(f"{primaryNumber}K são exatamente {KelvinConvertor2}° fahrenheit.")
    else:
        print("Você não utilizou nenhuma das possibilidades disponiveis!")
else:
    print("Esse conversor não aceita numeros nulos ou abaixo de 1.")