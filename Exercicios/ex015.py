km = float(input('Quantos KM você percorreu? '))
dia = float(input('Utilizou o carro por quantos dias? '))
valor = (km * 0.15) + (dia * 60)
print('Você deve pagar: {:.2f}R$'.format(valor))