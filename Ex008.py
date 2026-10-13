m = float(input('Digite uma medida em metros: '))
mm = m*1000
cm = m*100
dm = m*10
dam = m/10
hm = m/100
km = m/1000

print(f'O valor em metros colocado foi: {m:.2f}.\nSua conversão em milímetros é: {mm:.2f}.\nEm centímetros é {cm:.2f}.\nEm decímetros é {dm:.2f}\nEm decâmetros é {dam:.2}. Em hectômetros é {hm:.2f}.\nE em quilómetros é {km:.2f}.')