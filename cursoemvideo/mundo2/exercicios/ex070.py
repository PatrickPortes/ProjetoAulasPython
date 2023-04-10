# Estatísticas em Produtos

total = total1000 = cont = menor = 0
barato = ''

while True:
    nomeProd = str(input('Qual o Nome do Produto? ')).strip()
    precoProd = float(input('Qual o Preço do Produto? R$'))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nVocê quer Continuar? [S/N] ')).strip().upper()[0]

    cont +=1
    total += precoProd

    if precoProd > 1000:
        total1000 += 1

    if cont == 1 or precoProd < menor:
        menor = precoProd
        barato = nomeProd

    if continuar == 'N':
        break
print('FIM')

print(f'O Total Gasto na Compra foi: R${total}')
print(f'O Total de Produtos que Custam mais de R$1000 foi de: {total1000}')
print(f'O Nome do Produto mais Barato é: {barato} e seu preço é de {menor:.2f}')
