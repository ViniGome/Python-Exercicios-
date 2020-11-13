nome = str(input('Digite o seu nome completo: ')).strip()
name = nome.split()
print('Primeiro nome: {}'.format(name[0]))
print('Último nome: {}'.format(name[len(name)-1]))
