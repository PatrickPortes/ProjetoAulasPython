# Aprovando Empréstimo

casa = float(input('Qual o Valor da Casa? R$'))

salario = float(input('Qual o Salário do Comprador? R$'))

anos = int(input('Em Quantos Anos de Financiamento? '))

prestacao = casa / (anos * 12)

print('Para Pagar uma Casa de R${:.2f} em {} Anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))

minimo = (salario * 30) / 100

if prestacao > minimo:
    print('Você Não Pode Fazer esse Empréstimo!')
elif prestacao <= minimo:
    print('Você Pode Realizar o Empréstimo!')