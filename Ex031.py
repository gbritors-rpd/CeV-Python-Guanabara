dist = float(input('Digite a distância de viagem planejada em km: '))

if dist <= 200:
    val = dist * 0.5
else:
    val = dist * 0.45
print (f'O valor da sua viagem será de R$ {val:.2f} reais.')