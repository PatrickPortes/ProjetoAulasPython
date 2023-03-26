# Seno, Cosseno e Tangente

import math

ang = float(input('Digite o Ângulo: '))

sin = math.sin(math.radians(ang))

cos = math.cos(math.radians(ang))

tan = math.tan(math.radians(ang))

print(f'O seno desse ângulo é: {sin:.2f}')
print(f'O cosseno desse ângulo é: {cos:.2f}')
print(f'A tangente desse ângulo é: {tan:.2f}')