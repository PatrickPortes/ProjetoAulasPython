# Dividindo Valores em Várias Listas

listaA = []
listaB = []
listaC = []

while True:
    num = (int(input('\nDigite um Número: ')))

    if num % 2 == 0:
        listaA.append(num)
        listaB.append(num)
    else:
        listaA.append(num)
        listaC.append(num)

    continuar = str(input('Você Gostaria de Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('FIM')

print(f'ListaA: {listaA}')
print(f'\nListaB: {listaB}')
print(f'\nListaC: {listaC}')

# EXEMPLO DE OUTRA MANEIRA DE RESOLVER ESSE ALGORITMO:
'''
for i, v in enumerate(listaA):
    if v % 2 == 0:
        listaB.append(v)
    if v % 2 == 1:
        listaC.append(v)
'''

