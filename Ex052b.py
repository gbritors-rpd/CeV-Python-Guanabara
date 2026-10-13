n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[02;33m', end = ' ')
        cont += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{c}', end = ' ')
print('\033[m')
print(f'O valor {n} foi divisível {cont} vezes.')
if cont == 2:
    print(f'Portanto,{n} é um número PRIMO.')
else:
    print(f'Portanto {n} NÃO É um número primo.')