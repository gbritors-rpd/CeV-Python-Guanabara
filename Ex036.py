val = float(input('Qual o valor da casa que deseja comprar? R$'))
Sal = float(input('Qual o seu salário? R$'))
T = int(input('Em quantos anos você planeja pagar a casa? '))
m = T*12 #quantidade de parcelas
p = val/m

print(f'Com o salário de R$ {Sal:.2f} o seu empréstimo foi:', end=' ')

if p > Sal*0.3:
    print('\033[4;31mNEGADO\033[m')
    print('Por favor, consulte nossos planos e seu gerente.')
else:
    print('\033[4;32mAPROVADO\033[m')
    print(f'Seu pagamento será de R$ {p:.2f} reais mensais. Nosso gerete de empréstimos entrará em contato com você para acerto dos detalhes.')
