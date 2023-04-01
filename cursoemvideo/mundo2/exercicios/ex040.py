# Aquele Clássico da Média

n1 = float(input('Digite a sua Primeira Nota: '))
n2 = float(input('Digite a sua Segunda Nota: '))

m = (n1 + n2) / 2

if m >= 7.0:
    print('ALUNO APROVADO!!!')
elif m < 5.0:
    print('ALUNO REPROVADO!!!')
elif m >= 5.0 and m <= 6.9:
    print('ALUNO EM RECUPERAÇÃO!!!')
