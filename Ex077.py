palavras = ('Pedagogico', 'Caderno', 'Lapis', 'Aulas', 'Apostila', 'Prova', 'Caneta')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
    print(' ')