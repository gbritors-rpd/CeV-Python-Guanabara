
conthomem = 0
contmulher20 = 0
cont18 = 0
while True:
    print('-'*30)
    print('Cadastro de pessoas')
    print('-'*30)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in ('F', 'M'):
        sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher20 += 1

    print('-'*30)
    resp = ' '
    while resp not in ('S', 'N'):
        resp = str(input('Deseja continuar o cadastro de pessoas? {S/N] ')).upper().strip()
    if resp == 'N':
        print('Perfeito. Programa ENCERRADO.')
        break
print(f'O total adultos cadastrados foi {cont18}, sendo {conthomem} homens e {contmulher20} mulheres com menos de 20 anos.')

