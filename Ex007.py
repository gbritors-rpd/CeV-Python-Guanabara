nome1 = input('Digite o nome do primeiro aluno: ')
n11 = int(input('Digite a primeira nota: '))
n12 = int(input('Digite a segunda nota: '))
m1 = (n11 + n12)/2

nome2 = input('Digite o nome do segundo aluno: ')
n21 = int(input('Digite a primeira nota: '))
n22 = int(input('Digite a segunda nota: '))
m2 = (n21 + n22)/2

print(f'As notas de {nome1} foram: {n11} e {n12}.\nSua média foi: {m1:.1f}.')
print(f'As notas de {nome2} foram: {n21} e {n22}.\nSua média foi: {m2:.1f}.')
print('Então, podemos afirmar que', end=' ')
if m1 > m2:
    print(f'o aluno {nome1} teve maior média que o aluno {nome2}.')
else:
    print(f'o aluno {nome2} teve maior média que o aluno {nome1}.')