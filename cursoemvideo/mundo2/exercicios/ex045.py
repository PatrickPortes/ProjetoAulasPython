# Game: Pedra, Papel e Tesoura

import random
from time import sleep

print('-'*8)
print('JOKENPO GAME:')
print('-'*8)

lista= 'PEDRA', 'PAPEL', 'TESOURA'
botChoice = random.choice(lista)

playerChoice = str(input('Escolha Entre Pedra, Papel ou Tesoura: \n').upper().strip())

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*11)

print(f'\nO Player Escolheu: {playerChoice}')
print('------------------VS------------------')
print(f'O Computador Escolheu: {botChoice}\n')

#PLAYER EMPATA:
if botChoice == playerChoice:
    print('EMPATE!!!')
#PLAYER PERDE:
elif botChoice == 'PEDRA' and playerChoice == 'TESOURA' or \
        botChoice == 'PAPEL' and playerChoice == 'PEDRA' or \
            botChoice == 'TESOURA' and playerChoice == 'PAPEL':
    print('VOCÊ PERDEU!!!')
#PLAYER GANHA:
elif botChoice == 'PEDRA' and playerChoice == 'PAPEL' or \
        botChoice == 'PAPEL' and playerChoice == 'TESOURA' or \
            botChoice == 'TESOURA' and playerChoice == 'PEDRA':
    print('PARABÉNS!!! VOCÊ GANHOU!!!')



'''A LISTA E O IMPORT PODERIAM TER SIDOS UTILIZADOS DESSA OUTRA FORMA TBM:
        itens= ('pedra', 'papel', 'tesoura')
        computador = randInt(0,2)'''


