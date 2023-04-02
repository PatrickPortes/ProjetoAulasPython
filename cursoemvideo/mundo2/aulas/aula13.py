# Estrutura de Repetição FOR

#Exemplo 1:
for c in range(0,6):
    print('Oi')
print('FIM')


#Exemplo 2:
for c in range(0,6,2):
    print(c)
print('FIM')


#Exemplo 3:
for c in range(6,0,-1):
    print(c)


#Exemplo 4:
n = int(input('Digite um Número: '))
for c in range(0,n+1):
    print(c)


#Exemplo 5:
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)


#Exemplo 6:
s = 0
for c in range(0,3):
    n = int(input('Digite um Número: '))
    s += n
print(f'O Somatório de Todos os Números foi: {s}')
print('FIM')
