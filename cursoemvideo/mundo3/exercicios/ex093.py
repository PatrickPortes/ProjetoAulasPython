# Cadastro de Jogador de Futebol

print('-='*40)
print(f'{"CADASTRO DE JOGADOR DE FUTEBOL:":^75}')
print('-='*40)

jogador = dict()
partidas = list()

jogador['nome'] = str(input('\nQual o Nome do Jogador: '))

tot = int(input(f'Quantas Partidas {jogador["nome"]} Jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos Gols {jogador["nome"]} fez na {c+1}ª Partida? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*20)
print('')
print(jogador)

print('')
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('')
print('-='*20)
print(f'O Jogador {jogador["nome"]} Jogou {len(jogador["gols"])} Partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   -> Na Partida {i+1}, fez {v} gols!!!')
print(f'Foi um Total de {jogador["total"]} Gols!!!')
