menor = 0
maior = 0
for c in range (1,6):
    p = float(input(f'Por favor, digite o peso da {c}ª pessoa: '))
    if c == 1:
        menor = p
        maior = p
    else:
        if p < menor:
            menor = p
        if p > maior:
            maior = p
print(f'O maior peso lido foi {maior} kg.\nO menor peso lido foi {menor} kg.')