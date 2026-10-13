from time import sleep
from random import randint
cont = 0
print('-='*40)
print('HORA DE JOGAR. IMPAR OU PAR?'.center(40))
print('-='*40)
while True:
    n = -1
    while n < 0 or n > 9:
        n = int(input('Diga um valor (0 a 10): '))
    j = ' '
    while j not in 'PpIi':
       j = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()
    pc = randint(0 , 10)
    soma = n + pc
    if soma % 2 == 0:
        res = 'P'
    else:
        res = 'I'
    print(f'Você escolheu {n} e eu escolhi {pc}. A soma deu {soma}. Ou seja, deu {res}!')
    sleep(1)
    print('Ou seja...')
    sleep(1)
    if j == res:
        cont +=1
        print('Você ganhou! Próxima:')
        sleep(1)
        print('-=' * 40)
    else:
        print('Você PERDEU!')
        sleep(1)
        print(f'Você ganhou {cont} vezes.')
        sleep(1)
        print('FIM DE JOGO!')
        break

