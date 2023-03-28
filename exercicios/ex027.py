# Primeiro e Ultimo Nome de uma Pessoa

name = str(input('Digite seu Nome Completo: ')).strip()


n = name.split()

print('Seu primeiro nome é {}'.format(n[0]))

print('Seu último nome é {}'.format(n[len(n)-1]))
