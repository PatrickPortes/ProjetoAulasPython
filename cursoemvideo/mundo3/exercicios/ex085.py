# Lista com Pares e Ímpares

numeros = [[], []]

valor = 0

for n in range(1,8):
    valor = int(input(f'Digite o {n}ª Valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'Todos os Valores Digitados: {numeros}')

numeros[0].sort()
numeros[1].sort()
print(f'Valores Pares em Ordem Crescente: {numeros[0]}')
print(f'Valores Ímpares em Ordem Crescente: {numeros[1]}')

print('FIM')