from time import sleep
cont = 1
while True:
    n = int(input('Qual tabuada deseja ver? '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n*cont}')
        sleep(0.3)
        cont += 1
    print('-' * 30)
    print('Selecione outro número. Se desejar parar, selecione negativo.')
    print('-' * 30)
    cont = 1
    sleep(2)

print('-'*30)
print('Encerrando...')
sleep(2)