# SUPER Progressão Aritmética  V3.0

print('='*34)
print('OS 10 PRIMEIROS TERMOS DE UMA PA:')
print('='*34)

primeirot = int(input('\nQual o Primeiro Termo de uma PA? \n'))

razao = int(input('Qual é a Razão d uma PA? \n'))

termo = primeirot

cont = 1

total = 0

mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos Termos Você Quer Mostrar a Mais? '))
print(f'\nProgressão Finalizada com {total} Termos Mostrados!!!')
print('\nFIM')
