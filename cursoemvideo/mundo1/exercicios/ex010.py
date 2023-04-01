# Conversor de Moedas

cart = float(input('Quantos dinheiro você tem na sua carteira: R$ '))

dol = float(cart / 3.27)

print('Você pode comprar $ {:.2f} dólares com R$ {:.2f} reais na sua carteira!!!'.format(dol, cart))