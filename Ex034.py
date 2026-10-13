sal = float(input('Digite o seu salário atual: '))

if sal > 1250:
    nsal = sal*1.1
else:
    nsal = sal*1.15

print(f'Seu novo salário será de R$ {nsal:.2f} reais.')