from datetime import datetime

ano_nascimento = int(input('Em qual ano você nasceu?')) 
mes_nascimento = int(input('Em qual mês você nasceu?'))
dia_nascimento = int(input('Em qual dia você nasceu?'))

data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
data_atual = datetime.now()

diff = data_atual - data_nascimento


dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias  = dias // 30, dias % 30 


print(f'Você tem {anos} anos, {meses} meses e {dias} dias!.')