# Extraindo Dados de uma Lista

lista = []

contador = 0

while True:
    num = lista.append(int(input('\nDigite um Número: ')))
    contador += 1
    continuar = str(input('Você Gostaria de Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('FIM')

print(f'\nForam Digitados um Total de {contador} Números!!!')

lista.sort(reverse=True)
print(f'\nOs Números Digitados de Forma Decrescentes: {lista}')

if 5 in lista:
    print('\nO Número 5 foi Digitado!!!')
else:
    print('\nO Número 5 NÃO foi Digitado!!!')