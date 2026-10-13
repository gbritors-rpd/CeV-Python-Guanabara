menu = ('Suco', 5, 'Pipoca', 2.5, 'Chocolate', 4.5, 'Hamburguer', 10, 'Água', 2.75, 'Bala', 0.5, 'Amendoim', 7)
print('-=-'*15)
print('MENU'.center(45))
print('-=-'*15)
for c in range(0, len(menu), 2):
    print(f'{menu[c]:-<37} R$ {menu[c+1]:>4.2f}'. replace('.', ','))