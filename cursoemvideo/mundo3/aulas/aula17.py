# Listas (Parte 1)

'''
Tuplas são Imutáveis, mas as Listas são Mutáveis!!!
'''

# Exemplo 1:

sobremesas = ['bolo', 'brigadeiro', 'goiabada', 'torta', 'sorvete']

# Adicionando Itens na Lista
sobremesas.append('cookie')

# Adicionando em uma Posição Específico da Lista
sobremesas.insert(0,'paçoca')

# Apagar Elementos
del sobremesas[3]
#sobremesas.pop(3) # Normalmente o pop elimina o ultimo elemento, mas da pra especificar o índice em ()
#sobremesas.remove('goiabada')

# Verificando se o conteúdo existe na lista para deletar
if 'goiabada' in sobremesas:
    sobremesas.remove('goiabada')

# Criando Listas Através de Ranges
valoresRange = list(range(4,11))     # 4 5 6 7 8 9 10
valores = [10, 3, 2, 7, 1, 9, 6, 8, 4, 5]

# Ordenando Valores (Ordem Crescente)
valores.sort()

# Ordenando Valores (Ordem Decrescente)
valores.sort(reverse=True)

# Quantidade de Elementos
# print(f'{len(valores)}')

# Exemplo 2: (Exibindo Valores)
valores2 = []
valores2.append(5)
valores2.append(9)
valores2.append(4)

for v in valores2:
    print(f'{v}...', end=' ')

# Exemplo 3: (Exibindo Indices da Lista)
for c, v in enumerate(valores2):
    print(f'Na Posição {c}: Temos o Elemento {v}...', end=' ')

# Exemplo 4:
valores3 = list()
for cont in range(0,5):
    valores3.append(int(input('\nDigite um Valor para Adicionar na Lista: ')))
print(valores3)


# Exemplo 5: (Ligação de uma Lista em Outra)
a = [1, 2, 3, 4]
b = a
print(f'Lista A= {a}')
print(f'Lista B= {b}')
b[2]= 1000
print('-'*20)
print(f'Lista A= {a}')
print(f'Lista B= {b}')

# Exemplo 5: (Cópia de uma Lista em Outra)
print('-'*20)
a2 = [1, 2, 3, 4]
b2 = a2[:]
'''Pede para B receber uma cópia de valores de A (":" = fatiamento),
   com isso podendo mudar B posteriormente sem alterar A (cópia).'''
b2[2]= 1000
print('-'*20)
print(f'Lista A= {a2}')
print(f'Lista B= {b2}')
