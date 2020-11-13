real = float(input('Quantos reais você tem? R$'))
dolar = real / 5.74
print('Com R${:.2f}, você pode comprar: US${:.2f}'.format(real, dolar))