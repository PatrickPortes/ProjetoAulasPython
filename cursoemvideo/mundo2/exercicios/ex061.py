# Progressão Aritmética  V2.0

print('='*34)
print('OS 10 PRIMEIROS TERMOS DE UMA PA:')
print('='*34)

primeirot = int(input('\nQual o Primeiro Termo de uma PA? \n'))

razao = int(input('Qual é a Razão d uma PA? \n'))

termo = primeirot

cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1
print('FIM')
