from datetime import date
num = int(input('Digite o ano que deseja analisar. Para o ano atual, digite 0: '))
if num == 0:
    num = date.today().year
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print(f'O ano {num} é ano BISSEXTO.')
else:
    print (f'O ano {num} não é um ano BISSEXTO.')
