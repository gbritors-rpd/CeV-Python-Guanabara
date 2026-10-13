from random import randint
from time import sleep
npc = randint(0, 5)

print ('='*50)
print('Vou pensar em um valor de 0 a 5. Tente adivinhar qual!')
print('='*50)
p = int(input('Digite um valor de 0 a 5: '))
print('Processando...')
sleep(3)

print('PARABÉNS! Você escolheu o mesmo número que eu!' if npc == p else f'Hihihi. Você errou! Eu escolhi o número {npc}, não o número {p}')