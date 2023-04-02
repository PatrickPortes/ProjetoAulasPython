# Analisador Completo

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ""
totMulher50 = 0

for pessoa in range(1,5):
    print(f'\n===== {pessoa}º PESSOA =====')
    nome = str(input('Digite seu Nome: ')).strip()
    idade = int(input('Digite sua Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 45:
        totMulher50 += 1

mediaIdade = somaIdade / 4
print(f'A Média de Idade do Grupo de 4 Pessoas é de {mediaIdade} anos')

print(f'O Homem Mais Velho tem {maiorIdadeHomem} Anos e se Chama {nomeVelho}.')

print(f'Ao Todo são {totMulher50} Mulheres com Menos de 45 anos')