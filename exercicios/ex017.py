# Catetos e Hipotenusa

import math

oposto = float(input('Qual o comprimento do cateto oposto do triângulo retângulo? '))

adjacente = float(input('Qual o comprimento do cateto adjacente do triângulo retângulo? '))

#hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)

hipotenusa = math.hypot(oposto, adjacente)

print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')
