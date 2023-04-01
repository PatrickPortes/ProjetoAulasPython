# Comparando Números

n1 = int(input('Digite o Primeiro Número Inteiro: '))

n2 = int(input('Digite o Segundo Número Inteiro: '))

if n1 > n2:
    print(f'O Número {n1} é maior que o Número {n2}.')
elif n2 > n1:
    print(f'O Número {n2} é maior que o Número {n1}.')
elif n1 == n2:
    print(f'Os Números {n1} e {n2} são Iguais.')

