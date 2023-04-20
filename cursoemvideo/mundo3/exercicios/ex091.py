# Jogo de Dados em Python

from random import randint
from time import sleep
from operator import itemgetter

print('-='*32)
print(f'{"JOGO DE DADOS:":^60}')
print('-='*32)

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

ranking = list()

print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'O {k} Tirou o Número {v} no Dado!!!')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*16)
print(f'{"PLAYERS RANKING:":^30}')
print('-='*16)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

print('\nFIM')

