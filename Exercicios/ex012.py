valor = float(input('Digite o valor do produto: R$'))
desc = valor - (valor * 5 / 100)
print('Este produto que custava {}R$, com desconto de 5% na liquidação vai custar: {}R$'.format(valor, desc))