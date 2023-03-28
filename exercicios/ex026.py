# Primeira e Última Ocorrência de uma String

frase = str(input('Digite uma Frase: ').upper().strip())

print('A Letra A aparece {} nessa frase!'.format(frase.count('A')))


print('A Letra A aparece na posição {} pela primeira vez nessa frase!'.format(frase.find('A')+1))


print('A Letra A aparece na posição {} pela última vez nessa frase!'.format(frase.rfind('A')+1))




