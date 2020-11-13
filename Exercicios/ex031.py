viagem = float(input('Qual a distância da viagem? '))
print('Sua viagem será de {}Km'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('Sua viagem sairá por {}R$'.format(preço))
