# Analisando Triângulo v1.0

r1 = float(input('Primeiro Segmento do Triângulo: '))
r2 = float(input('Segundo Segmento do Triângulo: '))
r3 = float(input('Terceiro Segmento do Triângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos Acima Podem Formar Triângulo!')
else:
    print('Os Segmentos Acima Não Podem Formar Triângulo!')