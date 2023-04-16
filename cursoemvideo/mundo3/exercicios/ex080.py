# Lista Ordenada Sem Repetições

numeros = list()

maior = 0

for num in range(0, 5):
    n = int(input('Digite um Valor: '))

    if num == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao Final da Lista!!!')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na {pos+1}ª Posição da Lista!!!')
                break
            pos += 1

print(f'\nLista dos Valores em Ordem Crescente = {numeros}')
