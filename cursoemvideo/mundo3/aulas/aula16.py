# Tuplas

'''
Na nova att do python é possível usa-la sem parênteses!
        tuplas(), listas[], dicionário{}
'''

# Exemplo 1:

#comida = ('Hamburguer', 'Pizza', 'Suco', 'Pudim')
lanches = 'Hamburguer', 'Pizza', 'Suco', 'Pudim'
print(lanches[-2])
print(lanches[1:3])
print(lanches[2:])
print(lanches[:2])
print(lanches[-3:])


# Tuplas são Imutáveis - Error:
#comida[2]= 'Refrigerante'


# Exemplo 2:

for comida in lanches:
    print(f'Eu vou Comer {comida}')
print('Comi pra Caramba!')


# Exemplo 3:

for cont in range(0, len(lanches)):
    print(f'Eu vou Comer {lanches[cont]} na posição {cont}!')
print('Comi pra Caramba!')


# Exemplo 4:

for pos, comida in enumerate(lanches):
    print(f'Eu vou Comer {comida} na posição {pos}!')
print('Comi pra Caramba!')


# Exemplo 5:

# Ordenando
print(sorted(lanches))
print(lanches)


# Exemplo 6:

a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a

print(c)
print(d)
print(len(c))
print(c.count(5))
print(c.index(5))
print(c.index(5,1))


# Exemplo 7:

# Deletando
tupla = 'a', 'b', 'c', 'd'
del(tupla)
print(tupla)