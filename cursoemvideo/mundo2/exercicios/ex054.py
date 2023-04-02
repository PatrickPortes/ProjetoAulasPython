# Grupo Da Maioridade

from datetime import date

atual = date.today().year

totalmenor = 0
totalmaior = 0

for pessoa in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))

    idade = atual - nasc

    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade!!!'.format(totalmaior))
print('Ao todo tivemos {} pessoas menores de idade!!!'.format(totalmenor))
