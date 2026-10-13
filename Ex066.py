cont = 0
soma = 0

while True:
    n = int(input('Digite um valor: '))
    print('')
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} valores e sua soma final é {soma}.')