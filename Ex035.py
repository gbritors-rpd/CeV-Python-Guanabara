l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print(f'Os valores pertencem a um triangulo', end = ' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print(f'Os valores não pertencem a um triangulo.')