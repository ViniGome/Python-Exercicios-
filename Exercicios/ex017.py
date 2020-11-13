import math
co = float(input('Comprimento do cateto oposto é: '))
ca = float(input('Comprimento do cateto adjacente é: '))
hip = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hip))