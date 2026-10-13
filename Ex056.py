s = 0
velho = 0
m = 0
for c in range(1,5):
    print(f'{c}ª PESSOA'.center(20, '-'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    m += idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nvelho = nome
    if sexo == 'F' and idade < 20:
        s += 1
print(f'A média de idade do grupo é de {m/4} anos.\nO nome do homem mais velho é {nvelho}.\nEste grupo possui {s} mulheres com menos de 20 anos.')