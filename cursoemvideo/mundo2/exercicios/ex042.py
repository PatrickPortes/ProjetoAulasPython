# Analisando Triângulo v2.0

r1 = float(input('Primeiro Segmento do Triângulo: '))
r2 = float(input('Segundo Segmento do Triângulo: '))
r3 = float(input('Terceiro Segmento do Triângulo: '))

# Nesse ex eu poderia ter utilizado também a comparação de diferença (!=)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos Acima Podem Formar Triângulo!')
    if r1 == r2 == r3:
        print('O Triângulo será Equilátero: Todos os Lados Iguais!!!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O Triângulo será Isósceles: Dois Lados Iguais!!!')
    else:
        print('O Triângulo será Escaleno: Todos os Lados Diferentes!!!')
else:
    print('Os Segmentos Acima Não Podem Formar um Triângulo!')