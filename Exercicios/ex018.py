import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {}°, tem o Seno de: {:.2f}'.format(ang, seno))
print('O ângulo de {}°, tem o Cosseno de: {:.2f}'.format(ang, cosseno))
print('O ângulo de {}º, tem o Tangente de: {:.2f}'.format(ang, tangente))
