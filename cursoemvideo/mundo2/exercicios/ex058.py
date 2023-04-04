# Jogo de Adivinhação v2.0

import random

rnum = random.randint(0,10)

print('Sou seu Computado!!! Pensei em um Número entre 0 e 10, Tente Adivinhar!!!')

acertou = False

palpites = 1

while not acertou:
    num = int(input('Escolha um Número entre 0 e 10: '))
    if num == rnum:
        acertou = True
        print(f'Seu Número Escolhido ({num}) é Igual ao Número Pensado ({rnum})!!!')
        print(f'Você Levou {palpites} Tentativas para Acertar!!!')
    elif num > 10 or num < 0:
        print(f'Número Digitado Inválido!!! Escolha Entre 0 e 10')
    else:
        if num < rnum:
            print('MAISSS...')
        else:
            print('MENOSS...')
        print(f'Seu Número Escolhido ({num}) NÃO é Igual ao Número Pensado. Tente Novamente!!!')
        palpites += 1


''' OUTRA FORMA:
if rnum == num:
    print(f'Seu Número Escolhido ({num}) é Igual ao Número Sorteado ({rnum})!!!')
else:
    print(f'Seu Número Escolhido ({num}) NÃO é Igual ao Número Sorteado. Tente Novamente!!!')

while rnum != num:
    num = int(input('Escolha Novamente um Número entre 0 e 10: '))

    if rnum == num:
        print(f'Seu Número Escolhido ({num}) é Igual ao Número Sorteado ({rnum})!!!')
    else:
        print(f'Seu Número Escolhido ({num}) NÃO é Igual ao Número Sorteado. Tente Novamente!!!')
'''