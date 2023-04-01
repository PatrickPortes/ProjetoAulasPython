# Ano Bissexto

year = int(input('Digite um Ano: '))

if year % 4 == 0:
    print(f'O Ano {year} é Bissexto!')
else:
    print(f'O Ano {year} NÃO é Bissexto!')