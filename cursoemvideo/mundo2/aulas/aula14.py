# Estrutura de Repetição While

'''
for c in range(1,10):
    print(c)
print('FIM')
'''

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')


r = 'S'
while r == 'S':
    n = int(input('Digite um Valor: '))
    r = str(input('Quer Continuar? [S/N] ')).upper()
print('FIM')


num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um Número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram Digitados {par} Números Pares e {impar} Números Ímpares!!!')
print('FIM')


