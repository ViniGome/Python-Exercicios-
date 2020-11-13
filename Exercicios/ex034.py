salário = float(input('Digite seu salário atual: '))
if salário <= 1250.00:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 /100)
print('Seu novo salário é {:.2f}R$'.format(novo))