# Detector de Palíndromo

frase = str(input('Digite uma Frase: ')).strip().upper()

separando = frase.split()
juntando = ''.join(separando)

inverso = ''

for letra in range(len(juntando) -1,-1,-1):
    inverso += juntando[letra]
print(f'O inverso de {juntando} é {inverso}')

if inverso == juntando:
    print('A Frase Digitada É um Palíndromo!!!')
else:
    print('A Frase Digitada NÃO é um Palíndromo!!!')


# OUTRA FORMA DE REALIZAR ISSO SEM UTILIZAR O FOR (UTILIZA FATIAMENTO):
'''inverso = juntando[::-1]'''