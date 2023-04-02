# Contagem de Pares

print('Números Pares no Intervalo entre 1 e 50:')

for c in range(1,51): #Poderia tirar o if e fazer range(2,51)
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')