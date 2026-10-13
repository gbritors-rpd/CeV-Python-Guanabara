print('='*40)
print('Comparação numérica'.center(40))
print('='*40)

n1 = int(input('Por favor, escreva um número inteiro: '))
n2 = int(input('Por favor, selecione outro número inteiro: '))

if n1 > n2:
    msg = 'MAIOR QUE o'
elif n1 < n2:
    msg = 'MENOR QUE o'
else:
    msg = 'IGUAL ao'

print(f'O primeiro número [{n1}] é \033[2;31m{msg}\033[m segundo número [{n2}].')