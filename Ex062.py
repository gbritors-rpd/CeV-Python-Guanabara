n1 = int(input('Digite o número inicial da Progressão Aritmética: '))
r = int(input('Digite o valor da razão da PA: '))
c = 1
t = 10
total = 0
total
while t != 0:
    total += t
    while c <= t:
        if c < t:
            print(n1, end=' → ')
            n1 += r
            c += 1
        else:
            print(n1, '→ PAUSA')
            n1 += r
            c += 1
    t = int(input('Deseja continuar a PA? Quantos termos? Se quiser parar, digite 0: '))
    c = 1

print (f'FIM. Total de valores mostrados: {total}')