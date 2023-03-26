# Aluguel de Carros

days = float(input('Quantos dias o carro foi alugado? '))

km = float(input('Quantos km foram percorridos com o carro alugado? '))

total = (60 * days) + (0.15 * km)

print(f'O total a pagar pelo aluguel é de R${total}')