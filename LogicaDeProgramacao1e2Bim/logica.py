numero = '12367676453400090965127387343899548985688232768323579978972121139999'
qtd = 0
qtd2 = 0

for k in numero:
    qtd += 1

print(f"For > {qtd}")

while True:
    qtd2 += 1

    if qtd2 >= len(numero):
        print(f"While true > {qtd2}")
        break   


from time import sleep


var1 = 10

while True:
    sleep(1)

    print(f"While true2 > {var1}")
    var1 -= 1

    if var1 < 0:
        break

var2 = 10

for k in range(11):
    sleep(1)

    print(f"for 2 > {var2}")
    var2 -= 1

    if var2 < 0:
        break   


while True:
    try:
        sla = input("teste")
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")