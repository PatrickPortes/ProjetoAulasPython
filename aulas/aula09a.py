# Manipulando Texto


#Indice começa no 0
frase = str('Curso em Video Python')


# Fatiamento:
print(frase)
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])


# Análise:

# comprimento da frase
print(len(frase))

# contagem de qtd do char escolhido
print(frase.count('o'))

# contagem com fatiamento
print(frase.count('o', 0,13))

# encontrar
print(frase.find('deo'))
print(frase.find('Android')) #Quando o valor procurado n existe retorna -1

print('Curso' in frase)

# Transformação:

print(frase.replace('Python', 'Android'))

# Maiúsculo
frase.upper()

# Minúsculo
frase.lower()

# Primeira letra da string toda em maiúscula
frase.capitalize()

#Todas as primeiras letras das palavras maiúsculas
frase.title()

#Novo Exemplo:
frase2 = str('   Aprenda Python  ')

#remove espaço do inicio e do final da string
frase2.strip()
frase2.rstrip() # r = right
frase2.lstrip() # l = left


# Divisão:

#faz uma divisão baseado nos espaços das strings
print(frase.split())


# Junção:
print('-'.join(frase))

