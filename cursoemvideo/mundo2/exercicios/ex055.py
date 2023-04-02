# Maior e Menor da Sequência

maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input('Peso da {}ª Pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior= peso
        menor= peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O Maior Peso Lido foi de {maior}Kg')
print(f'O Menor Peso Lido foi de {menor}Kg')
