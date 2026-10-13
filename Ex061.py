n1 = int(input('Digite o número inicial da Progressão Aritmética: '))
r = int(input('Digite o valor da razão da PA: '))
c = 1
t = 10
while c <= t:
    if c < t:
        print(n1, end=' → ')
        n1 += r
        c += 1
    else:
        print(n1, '→ FIM')
        n1 += r
        c += 1



