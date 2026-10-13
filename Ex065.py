print('~'*60)
print('Média, Maior e Menor valor'.center(60))
print('~'*60)
soma = total = 0
resp = 's'
maior = 0

while resp in 'Ss':
    n = int(input('Digite um valor:    '))
    soma += n
    total += 1
    print (' ')
    resp = str(input('Deseja continuar? [S/N]  ')).strip().upper()
    print ('-'*60)
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou {total} valores e a média entre eles é {soma/total:.2f}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')