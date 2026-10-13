c = 0
t = 0
n = 0
while c != 999:
    n1 = int(input('Digite um valor: '))
    t += n1
    n += 1
    c = n1
    print(f'Seu valor é: {n1}.')

print(f'Você digitou {n-1} valores e a soma total dos deles é: {t-n1}')
