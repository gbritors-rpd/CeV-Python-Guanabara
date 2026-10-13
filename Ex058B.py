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
        if play > npc:
            dica = 'menor'
        elif play < npc:
            dica = 'maior'

        print(f'Você escolheu o número {ver}{play}{nor}.')
        play = int(input(f'Dica: meu número é um pouco {dica}! Faça um novo palpite: '))
        print('=' * 60)
        s += 1
print (f'Você acertou seu palpite na {s+1}ª vez!')
