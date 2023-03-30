# Jogo de Adivinhação v1.0

import random

rnum = random.randint(0,5)

num = int(input('Escolha um Número entre 0 e 5: '))

if rnum == num:
    print(f'Seu Número Escolhido ({num}) é Igual ao Número Sorteado ({rnum})!!!')
else:
    print(f'Seu Número Escolhido ({num}) NÃO é Igual ao Número Sorteado ({rnum})!!!')
