# Cálculo de Fatorial

from math import factorial

n = int(input('Digite um Número: '))

#Maneira com Import:
print(f'O Fatorial de {n} é: {factorial(n)}')


#Maneira Tradicional:
c = n
f = 1

print(f'Calculando Fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'{f}')
