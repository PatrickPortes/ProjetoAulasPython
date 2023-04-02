# Progressão Aritmética

print('='*34)
print('OS 10 PRIMEIROS TERMOS DE UMA PA:')
print('='*34)

primeirot = int(input('\nQual o Primeiro Termo de uma PA? \n'))

razao = int(input('Qual é a Razão d uma PA? \n'))

decimo = primeirot + (10-1) * razao

for c in range(primeirot, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')