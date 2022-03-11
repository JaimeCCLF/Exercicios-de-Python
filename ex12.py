valor = float(input('Qual é o preço do produto? R$'))
desconto = valor - (valor / 100 * 5)
print('O produto que custa R${:.2f} na promoção com desconto de 5% vai custar RS{:.2f}'.format(valor, desconto))
