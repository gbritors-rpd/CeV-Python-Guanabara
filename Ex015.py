d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quando quilômetros foram rodados? '))

v = (60*d)+(0.15*km)

print(f'O valor total do seu aluguel foi: R$ {v:.2f} reais.')