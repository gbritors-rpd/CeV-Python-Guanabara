from random import randint
npc = randint(0, 10)
s = 0
print('='*60)
print('Vamos jogar!'.center(60))
print('='*60)
play = int(input('Selecione um número de 0 a 10: '))
ver = '\033[4;31m'
ama = '\033[4;33m'
nor = '\033[m'
while play != npc:
    if play != npc:

        print(f'Você escolheu o número {ver}{play}{nor}. Eu escolhi o número {ama}{npc}{nor}.')
        npc = randint(0, 10)
        play = int(input('Vou mudar minha escolha! Faça um novo palpite: '))
        print('=' * 60)
        s += 1
print (f'Você acertou seu palpite na {s+1}ª vez! Escolhemos o mesmo número:\033[4;32m{npc}{nor}.')
