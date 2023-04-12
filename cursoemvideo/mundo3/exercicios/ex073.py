# Tuplas com Times de Futebol

times = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', \
        'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', \
        'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avai', 'Juventude'

print('='*42)
print('INFORMAÇÕES DO CAMPEONATO BRASILEIRO 2022:')
print('='*42)

print(f'\nOs Cincos Primeiros Colocados São: {times[0:5]}')

print(f'\nOs Quatro Últimos Colocados São: {times[-4:]}')

print(f'\nOs Times em Ordem Alfabética: {sorted(times)}')

print(f'\nO Corinthias está na {times.index("Corinthians")+1}ª Posição da Tabela!')

