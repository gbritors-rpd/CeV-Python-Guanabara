import math
from math import sqrt

co = float(input('Digite o valor do cateto oposto: '))
ca = int (input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(co,2) +pow(ca, 2))
hip2 = math.hypot(co, ca)

print (f'O valor da hipotenusa é {hipotenusa:.2f}')
print(f'O valor calculado da outra forma é {hip2:.2f}')

