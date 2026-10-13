from datetime import date
s = 0
for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento: '))
    if date.today().year - ano >= 21:
        s += 1
print(f'O número de pessoas que já atingiu a maioridade é {s}, enquanto {7-s} pessoas ainda não estão na maioridade.')