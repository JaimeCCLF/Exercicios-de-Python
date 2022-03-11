d = int(input('Quantos dias alugado? '))
km = int(input('Quantos Km rodados? '))
valor = (d*60)+(km * 0.15)
print('O total a pagar é de R${}'.format(valor))
