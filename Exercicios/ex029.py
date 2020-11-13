vel = float(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('Multado! Acima de 80Km/h')
    multa = (vel-80) * 7
    print('Você devera pagar uma multa de R${:.f}'.format(multa))
else:
    print('Velocidade aceitada!')