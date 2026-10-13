n1 = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão desejada para a Progressão aritmética: '))

for c in range(0, 10):
    print(n1, end = ' → ')
    n1 = n1+r

print('Fim da PA.')