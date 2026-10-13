from time import sleep
escolha = 0
print('='*60)
print('MENU MATEMÁTICO'.center(60,'-'))
n1 = float(input('Escolha um número:  '))
n2 = float(input('Escolha outro número:   '))
tempo = 'CALCULANDO...'.center(60)
while escolha < 5:
    print('=' * 60)
    print('OPÇÃO [1] - SOME OS VALORES')
    print('OPÇÃO [2] - MULTIPLIQUE OS VALORES')
    print('OPÇÃO [3] - QUAL O MAIOR VALOR?')
    print('OPÇÃO [4] - ESCOLHA NOVOS NÚMEROS.')
    print('OPÇÃO [5] - ENCERRAR O PROGRAMA')
    escolha = int(input((f'Escolha o que deseja fazer com os número {n1} e {n2}:'.center(60))))
    print (' ')

    print('=' * 60)
    if escolha == 1:
        print(tempo)
        sleep(2)
        print(f'A soma entre os valores é {n1 + n2}.'.center(60))
        print (' ')
        sleep(2)
    elif escolha == 2:
        print(tempo)
        sleep(2)
        print(f'O produto entre os valores é {n1 * n2}.'.center(60))
        print(' ')
        sleep(2)
    elif escolha == 3:
        if n1 == n2:
            print(tempo)
            sleep(2)
            print('Você escolheu números iguais!'.center(60))
            print(' ')
            sleep(2)
        else:
            if n1 > n2:
                maior = n1
                print(tempo)
                sleep(2)
                print(f'O maior número é {maior}.'.center(60))
                print(' ')
                sleep(2)
            else:
                maior = n2
                print(tempo)
                sleep(2)
                print(f'O maior número é {maior}.'.center(60))
                print(' ')
                sleep(2)
    elif escolha == 4:
        print('Ok, vamos mudar os valores.'.center(60))
        print(' ')
        sleep(2)
        n1 = float(input('Escolha um número:'.center(60)))
        n2 = float(input('Escolha outro número: '.center(60)))
        print(' ')
        sleep(2)
    else:
        print('Ok. Obrigado por participar.'.center(60))
        sleep(2)
        print('Encerrando...'.center(60))
        sleep(2)
