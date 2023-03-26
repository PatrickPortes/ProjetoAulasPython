# Sorteando um Item na Lista

import random

aluno1 = str(input('Digite o Nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o Nome do Segundo Aluno: '))
aluno3 = str(input('Digite o Nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o Nome do Quarto Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sortear = random.choice(lista)

print(f'O Aluno Escolhido pelo Sorteio foi: {sortear}')