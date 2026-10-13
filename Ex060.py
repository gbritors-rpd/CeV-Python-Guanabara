n1 = int(input('Digite um número para descobrir seu fatorial: '))
c = n1
m = 1
print(f'{n1}!', end = ' = ')
while c > 0:
    if c > 1:
        print(f'{c} x ', end = '')
        c -= 1
        m *= n1 - c
    else:
        print(f'{c}', end = ' = ')
        c -= 1
        m *= n1 - c
print(m)