# Maior e Menor Valores em Tupla

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os Números da Tupla são: {numeros}')

print(f'\nO menor valor é o número {min(numeros)}, e o maior é o número {max(numeros)}.')