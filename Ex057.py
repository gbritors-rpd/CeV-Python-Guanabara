sexo = str(input('Olá! Para iniciarmos o serviço, por favor:\nInsira o seu sexo [M/F/NB]: ')).strip().upper()

while sexo not in 'MFNB':

    sexo = str(input('Desculpe, esta não é uma entrada válida. As opções são:\nM - Masculino;\nF - Feminino;\nNB - Não binário.\n Por favor, preencha novamente: ')).strip().upper()

print ('Perfeito!')
print(f'Sexo {sexo} registrado com sucesso. Daremos sequência ao processo.')