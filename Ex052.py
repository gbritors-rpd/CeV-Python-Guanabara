n = int(input('Por favor, digite um número para vermos se ele é primo: '))
s = 0
for c in range(n, 1, -1):
    if n % c == 0:
        s += 1
if s == 1:
    print(f'O número {n} é um número primo. ')
else:
    print(f'O número {n} não é um número primo.')



