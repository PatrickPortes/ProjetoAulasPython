# Maior e Menor Valores

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terceiro Número: '))


# Verificação Maior

maior = n1

if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificação Menor

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O Maior Número: {maior}')
print(f'O Menor Número: {menor}')