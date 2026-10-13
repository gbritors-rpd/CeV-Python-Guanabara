n1 = int(input('Quantos valores da Sequência de Fibonacci deseja ver? '))
print('~'*60)
c = 2
f1 = 0
f2 = 1
print(f1, end = ' ')
print(f2, end = ' ')
while c <= n1:
    if c < n1:
        f3 = f1 + f2
        print(f'{f3}', end = ' - ')
        f1 = f2
        f2 = f3
    else:
        f3 = f1 + f2
        print(f'{f3}')
        print(f'Fim dos {n1} valores.'.center(60))
    c += 1
print('~'*60)