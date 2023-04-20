# Dicionário em Python

aluno = dict()

aluno['nome'] = str(input('Digite seu Nome: '))
aluno['media'] = float(input(f'Digite sua Média Escolar {aluno["nome"]}: '))

if aluno["media"] >= 7.0:
    #print(f'O Aluno {aluno["nome"]} foi aprovado!!!')
    aluno['situação'] = 'Aprovado'
else:
    #print(f'O Aluno {aluno["nome"]} foi reprovado!!!')
    aluno['situação'] = 'Reprovado'


for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')