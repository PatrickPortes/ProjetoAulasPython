# Aprimorando os Dicionários

# Cadastro de Jogador de Futebol

print('-='*40)
print(f'{"CADASTRO DE JOGADOR DE FUTEBOL APRIMORADO:":^75}')
print('-='*40)

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('\nQual o Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas {jogador["nome"]} Jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos Gols {jogador["nome"]} fez na {c+1}ª Partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO: Por favor, digite apenas S ou N.')
    if resp == 'N':
        break


print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')

print('')
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
print()

while True:
    busca = int(input('Mostrar Dados de Qual Jogador? (Digite 999 para Parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO: Não existe jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    - No Jogo {i+1} fez {g} gols.')
    print('-'*40)

print('\nFIM')
