# Classificando Atletas

ano = int(input('Qual o Ano de Nascimento do Atleta: '))

a = 2023 - ano

print(f'O Atleta tem {a} anos')

if a <= 9:
    print('CATEGORIA MIRIM')
elif a > 9 and a <= 14:
    print('CATEGORIA INFANTIL')
elif a > 14 and a <= 19:
    print('CATEGORIA JUNIOR')
elif a > 19 and a <= 20:
    print('CATEGORIA SENIOR')
elif a > 20:
    print('CATEGORIA MASTER')
