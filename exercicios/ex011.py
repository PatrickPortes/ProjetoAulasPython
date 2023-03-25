# Pintando Parede

lar = float(input('Qual a Largura da sua Parede em Metros? '))

alt = float(input('Qual a Altura da sua Parede em Metros? '))

#Calculando a área da parede
a = float(alt * lar)

#Quantidade de tinta para pintar (cada litro de tinta pinta uma área de 2m²)
qtd = float(a / 2)

#Resultado
print('A sua parede tem uma áre de {} m², e precisa de {} litros de tinta para pinta-la!!'.format(a, qtd))

