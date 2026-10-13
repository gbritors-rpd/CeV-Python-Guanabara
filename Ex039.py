from datetime import date
ano = int(input('Por favor, digite o ano do seu nascimento. [AAAA]: '))
idade = date.today().year - ano
dif = 18 - idade

if idade < 18:
    print('Você ainda não precisou se alistar.')
    print(f'Seu alistamento ocorrerá daqui a {dif} anos, ou seja, em {date.today().year + dif}.')
elif idade > 18:
    print('Você já deveria ter se alistado.')
    print(f'Seu alistamento deveria ter sido feito a {abs(dif)} anos, ou seja, em {date.today().year + dif}.')
else:
    print('Seu alistamento deverá ser realizado este ano!')