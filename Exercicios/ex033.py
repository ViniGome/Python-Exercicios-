a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
men = a
if b<a and b<c:
    men = b
if c<a and c<b:
    men = c
mai = a
if b > a and b > c:
    mai = b
if c > a and c > b:
    mai = c
print('O menor valor é: {}'.format(men))
print('O maior valor é: {}'.format(mai))
