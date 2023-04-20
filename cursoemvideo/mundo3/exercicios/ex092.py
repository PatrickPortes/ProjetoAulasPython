# Cadastro de Trabalhador em Python

from datetime import datetime

print('-='*40)
print(f'{"CADASTRO DE TRABALHADOR:":^75}')
print('-='*40)

dados = dict()

dados['nome'] = str(input('\nDigite seu Nome: '))
nasc = int(input('Digite seu Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Qual o Número da sua Carteira de Trabalho? (0 não tem) '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-='*30)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

print('\nFIM')
