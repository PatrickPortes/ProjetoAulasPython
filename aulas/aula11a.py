# Cores no Terminal

nome = 'Patrick'

cores = { 'limpa':'\033[m',
          'azul':'\033[m',
          'amarelo':'\033[m',
          'preto/branco':'\033[7:30m' }

print('Olá, Seja Muito Bem-Vindo!!! {}{}{}!!!'.format('\033[4:34m', nome, '\033[m'))


print('\n\033[0;30;41mTESTE\033[m')
print('\n\033[4;33;44mTESTE\033[m')
print('\n\033[1;35;43mTESTE\033[m')
print('\n\033[30;42mTESTE\033[m')
print('\n\033[mTESTE\033[m')
print('\n\033[7;30mTESTE\033[m')