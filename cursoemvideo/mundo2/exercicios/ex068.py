# Jogo do Par ou Ímpar

import random

print('-'*18)
print('PAR OR ÍMPAR GAME:')
print('-'*18)

playerChoice = botChoice = ''

start = str(input('\nVocê Quer Começar Escolhendo? [S/N] ')).strip().upper()

if start == 'S' or start == 'SIM':
    playerChoice = str(input('Escolha Par ou Ímpar? ')).strip().upper()
    if playerChoice == 'PAR':
        botChoice = 'IMPAR'
    else:
        botChoice = 'PAR'
else:
    print('OK, o Computador vai Escolher!!!\n')
    lista = 'PAR', 'IMPAR'
    botChoice = random.choice(lista)
    if botChoice == 'PAR':
        playerChoice = 'IMPAR'
    else:
        playerChoice = 'PAR'


print('='*20)
print(f'Player: {playerChoice}')
print('           X          ')
print(f'Computador: {botChoice}')
print('='*20)

soma = 0

while True:
    num = int(input('Digite seu Número: '))
    rnum = random.randint(0,11)
    soma = num + rnum
    if soma % 2 == 0:
        print(f'Você Jogou {num}, e o Computado Jogou {rnum}, Total de {soma} deu Par!!!')
        if playerChoice == 'PAR':
            print(f'PARABÉNS VOCÊ GANHOU!!! CONTINUE JOGANDO ATÉ PERDER!!!\n')
        else:
            print(f'O COMPUTADOR GANHOU!!! GAME OVER!!!')
            break
    elif soma % 2 != 0:
        print(f'Você Jogou {num}, e o Computado Jogou {rnum}, Total de {soma} deu Ímpar!!!')
        if playerChoice == 'IMPAR':
            print(f'PARABÉNS VOCÊ GANHOU!!! CONTINUE JOGANDO ATÉ PERDER!!!\n')
        else:
            print(f'O COMPUTADOR GANHOU!!! GAME OVER!!!')
            break

# Poderia ter sido utilizado o tratamento de:
'''
tipo = ''
while tipo not in 'PpIi'
    tipo = str(input('Par ou Impar? ')).strip().upper()[0]
'''