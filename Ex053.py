from shlex import join

f = str(input('Digite a frase que quer conferir se é um palíndromo: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for c in range(len(j)-1, -1,-1):
    i += j[c]

print(f'Sua frase é {f}, as palavras de trás para frente é: {i} .')
if i == j:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')