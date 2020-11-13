salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = salario + (salario*15/100)
print('O salário do funcionário que era: {:.2f}R$, com aumento de 15% passa a receber: {:.2f}R$'.format(salario, reajuste))