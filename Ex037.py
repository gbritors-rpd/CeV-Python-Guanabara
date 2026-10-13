from time import sleep
msg = 'Por favor, escreva o número a ser convertido: '
print('='*60)
n1 = int(input(msg.center(60)))
print('='*60)

print('[1] Para conversão em números binários.')
print('[2] Para conversão em números octais.')
print('[3] Para conversão em números hexadecimais.')
msg2 = 'Selecione a opção desejada:'.center(60,'-')
n = int(input(msg2))
print('CONVERTENDO.....')
sleep(3)

if n == 1:
    a = bin(n1)[2:]
    msg3 = 'binário'
    print(f'O número {n}, quando convertido para número {msg3}, é: {a}.')
elif n == 2:
    a = oct(n1)[2:]
    msg3 = 'octal'
    print(f'O número {n}, quando convertido para número {msg3}, é: {a}.')
elif n == 3:
    a = hex(n1)[2:]
    msg3 = 'hexadecimal'
    print(f'O número {n}, quando convertido para número {msg3}, é: {a}.')
else:
    print ('Desculpe, essa não é uma opção válida.')



