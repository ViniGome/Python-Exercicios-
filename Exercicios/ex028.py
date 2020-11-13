from random import randint
npc = randint(0, 5)
print('-*-' * 26)
print('Se adivinhar o número que eu estou pensando de 0 a 5 ganha um pastel!')
print('-*-' * 26)
n = int(input('Em que número eu estou pensando? '))
if n == npc:
    print('Você ganhou um pastel!')
else:
    print('Vai ficar sem pastel, eu pensei no número {}...'.format(npc))