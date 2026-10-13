n0 = int(input('Digite um valor: '))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
numeros = (n0, n1, n2, n3)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}ª posição.')
else:
    print('O número 3 não aparece na lista numérica.')
print('Os valores pares digitados foram: ', end = ' ')
for c in numeros:
    if c % 2 == 0:
        print(c, end = ' ')


