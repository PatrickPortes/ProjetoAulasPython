# Dicionários

dados = dict()

dados = {'nome': 'Patrick', 'idade': 23}

print(dados['nome'])
print(dados['idade'])


# Exemplo 1: (No caso do dicionário o método append não funciona)
dados['sexo']='M'
del dados['idade']


# Exemplo 2:
filme = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}

print(filme.values())   #Retorna os valores (conteúdo) do dicionário.
print(filme.keys())     #Retorna os nomes dos indíces do dicionário.
print(filme.items())    #Retorna os valores e chaves do dicionário.

# Exemplo 3:
for k, v in filme.items():  # (K= KEY, V= VALUE)
    print(f'O {k} é {v}')

# Exemplo 4:
pessoas = {'nome': 'Charles', 'sexo': 'M', 'idade': 32}
print(f'\nO {pessoas["nome"]} tem {pessoas["idade"]} anos!!!')      #tem q colocar em aspas duplas "" se não da erro se for simples ''
del pessoas['sexo']
pessoas['nome'] = 'Diogo'
pessoas['peso'] = 80
for k, v in pessoas.items():
    print(f'{k} = {v}')


# Exemplo 4: (Dicionário Dentro de uma Lista)

brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)


print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

# Exemplo 5:  (No dicionário não é possível realizar o fatiamento, para isso tem um método chamado copy)
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O Campo {k} tem o Valor {v}')
print('\nFIM')

