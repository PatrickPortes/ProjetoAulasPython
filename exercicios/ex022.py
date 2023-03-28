# Analisador de Texto

name = str(input('Digite o seu nome completo: ')).strip()


print(f'Seu Nome com Letras Maiúsculas: {name.upper()}')


print(f'Seu Nome com Letras Minúsculas: {name.lower()}')


print('Seu Nome tem no total {} letras'.format(len(name) - name.count(' ')))


#print('Seu primeiro nome é: {}'.format(name.find(' ')))
separa = name.split()
print('Seu primeiro nome é: {} e ele tem {} letras'.format(separa[0], len(separa[0])))






