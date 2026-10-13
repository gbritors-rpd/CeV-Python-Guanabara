vel = float(input('Qual a velocidade que você estava quando passou pelo radar? '))

if vel <= 80:
    print(f'Fique tranquilo, com a velocidade de {vel}km/h você não receberá multa!')
else:
    print(f'Sinto muito, mas a essa velocidade você receberá uma multa de R$ {(vel-80)*7}')
