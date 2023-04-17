# Listas (Parte 2)

# Exemplo 1
print('='*20)
print(' '*5, end='')
print('EXEMPLO 1:')
print('='*20)

dados = list()

dados.append('Patrick')
dados.append(23)

print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])

pessoas.append(['Maria', 19])
pessoas.append(['João', 32])

print(dados)
print(pessoas)

print(pessoas[0][0])    # Patrick
print(pessoas[1][1])    # 19
print(pessoas[2][0])    # João
print(pessoas[0])       # ['Patrick', 23]


# Exemplo 2
print('='*20)
print(' '*5, end='')
print('EXEMPLO 2:')
print('='*20)

'''
for p in pessoas:
    print(p)
'''

for p in pessoas:
    print(f'{p[0]} tem {p[1]} Anos de Idade!!!')


# Exemplo 3
print('='*20)
print(' '*5, end='')
print('EXEMPLO 3:')
print('='*20)

galera = list()
infos = list()

for c in range(0,2):
    galera.append(str(input(f'Digite o Nome da {c+1}ª Pessoa: ')))
    galera.append(int(input(f'Digite a sua Idade: ')))
    infos.append(galera[:])
    galera.clear()

print(infos)

totmaior = totmenor = 0

for p in infos:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!!!')
        totmaior +=1
    else:
        print(f'{p[0]} é menor de idade!!!')
        totmenor +=1

print(f'Temos um Total de {totmaior} Maior de Idade e {totmenor} Menor de Idade!!!')
print('\nFIM')
