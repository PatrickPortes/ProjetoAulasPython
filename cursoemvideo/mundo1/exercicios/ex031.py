# Custo da Viagem

km = float(input('Digite a Distância de uma Viagem em Km: '))

if km <= 200.0:
    price1 = 0.50 * km
    print(f'O preço da sua viagem será R${price1}')
else:
    price2 = 0.45 * km
    print(f'O preço da sua viagem será R${price2}')