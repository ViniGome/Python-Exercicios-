print('-*-' * 15)
print('Digite três valores para calcular um triângulo!')
print('-*-' * 15)
primeiro = float(input('Digite o primeiro segmento: '))
segundo = float(input('Digite o segundo segmento: '))
terceiro = float(input('Digite o terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Pode ser formado um triângulo')
else:
    print('Com os segmentos informados, não será possivel criar um triângulo.')