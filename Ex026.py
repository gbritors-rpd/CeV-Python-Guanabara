nome = str(input('Digite qualquer coisa que quiseres, baby: ')).upper().strip()

print ({len(nome)})
print(f'O número de letras "a" da sua sentença é {nome.count('A')}.')
print(f'A primeira letra "a" aparece na posição {nome.find('A')+1}.')
print(f'A última letra "a" aparece na posição {nome.rfind('A')+1}.')