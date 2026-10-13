import random
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
print('='*40)
print('Vamos jogar!!!'.center(40))
print('='*40)
print('[0] PEDRA [0]'.center(40))
print('[1] PAPEL [1]'.center(40))
print('[2] TESOURA [2]'.center(40))
pla = int(input('Escolha entre Pedra, Papel e Tesoura: '))
npc = random.randint(0,2)

print ('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
sleep(1)

if pla == npc:
    print('EMPATE! Tente novamente.')
    print(f'Nós dois escolhemos {item[pla]}!')
elif pla == 0 and npc == 1 or pla == 1 and npc == 2 or pla == 2 and npc == 0:
    print('PERDEU! Hihihi.')
    print(f'Você escolheu {item[pla]} e o computador escolheu {item[npc]}!')
else:
    print('Você GANHOU! Parabéns!')
    print(f'Você escolheu {item[pla]} e o computador escolheu {item[npc]}!')