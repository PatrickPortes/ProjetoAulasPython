# Interrompendo Repetições While

# Exemplo de Atualização do Python:
'''
nome = 'Patrick'
idade = 23

print(f'O {nome} tem {idade} anos.') # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print(f'O %s tem %d anos.' % (nome, idade)) # Python 2
'''

# Exemplo 1:
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('FIM')


# Exemplo 2:
n = s = 0
while n < 5:
    n = int(input('Digite um Número: '))
    s += n
print(f'A Soma Desses Números Vale: {s}')


# Exemplo 3:
n = s = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    s+=n
print(f'A Soma Desses Números Vale: {s}')


