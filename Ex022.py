nome = str(input ('Digite seu nome completo: ')).strip()

print(f'Seu nome, com maiúsculas, é: {nome.upper()}')
print(f'Seu nome, com minúsculas, é: {nome.lower()}')
print(f'Seu nome possui {len(nome) - nome.count(' ')} letras')

sep = nome.split()

print(f'Seu primeiro nome é {sep[0]}, e possui {len(sep[0])} letras')