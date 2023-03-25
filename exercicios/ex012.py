#Calculando Desconto

preco = float(input('Digite o preço do Produto: '))

desc = float( preco - preco * 0.05 )

#Poderia ser tbm:
# desc = preco - (preco * 5 / 100)

print(f'O produto com 5% de deconto ficará com o preço de R$: {desc:.2f}')