from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os números digitados foram: ', end = ' ')
for c in numeros:
    print(f'{c}', end = ' ')
print(f'\nO maior número digitado foi: {max(numeros)}.')
print(f'O menor número digitado foi: {min(numeros)}.')