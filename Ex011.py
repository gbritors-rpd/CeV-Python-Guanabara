b = float(input('Qual o comprimento (em metros) da sua parede? '))
a = float(input('Qual a altura (em metros) da sua parede? '))

area = a*b
tin = area//2
print(f'Considerando o comprimento {b:.1f} e a altura {a:.1f}, a área total de parede é {area:.1f}.\nPortanto, a quantidade necessária de tinta é:', end = ' ')
if area%2 == 0 :
    print(tin, 'galões.')
else:
    print(tin+1, 'galões, e terá um pouco de sobra.')