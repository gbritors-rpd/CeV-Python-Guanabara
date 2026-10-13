nome = str(input('Digite seu nome completo: ')).strip()
n = nome.upper()

print(n.find('SILVA') != -1)

print('silva' in nome.lower())