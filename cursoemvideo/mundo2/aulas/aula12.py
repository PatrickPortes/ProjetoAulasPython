# Condições Aninhadas

name = str(input('Qual o seu Nome? '))

if name == 'Patrick':
    print('Que Nome Bonito!')
elif name == 'Paulo' or name == 'Maria' or name == 'João':
    print('Seu Nome é Bem Comum no Brasil!')
else:
    print('Que Nome Normal!')

print(f'Seja Bem-Vindo e Tenha um Bom Dia, {name}')