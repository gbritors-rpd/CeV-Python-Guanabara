qntd = 0
cont1000 = 0
soma = 0

while True:
    print('-=' * 20)
    nome = str(input('Nome do produto: '.center (20)))
    preco = float(input('Valor do produto: R$ '.center (20)))
    qntd += 1
    soma += preco
    if preco > 1000:
        cont1000 += 1
    if qntd == 1:
        menor = preco
        nomemen = nome
    else:
        if preco < menor:
            menor = preco
            nomemen = nome
    resp = ' '
    while resp not in ('S', 'N'):
        resp = str(input('Quer continuar a cadastrar produtos no seu carrinho? [S/N] ')).strip().upper()
    if resp == 'N':
        break

print('-*-')
print(f'O valor final da sua compra ficou em: R${soma:.2f}.')
print(f'Você comprou {cont1000} produtos que custam acima de R$1000.00 reais.')
print(f'O produto mais barato que você comprou foi {nomemen}, que custou R$ {menor:.2f} reais.')