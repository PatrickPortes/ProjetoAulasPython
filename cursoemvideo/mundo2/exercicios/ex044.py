# Gerenciador de Pagamentos

preco = float(input('Digite o Valor do Preço da suas Compras: R$'))

print('\nEscolha Qual Será o Método de Pagamento: \n')

print('Digite 1 para À Vista dinheiro/cheque (10% de desconto) ')
print('Digite 2 para À Vista no cartão (5% de desconto) ')
print('Digite 3 para Em até 2x no cartão (preço normal) ')
print('Digite 4 para Em até 3x no cartão (20% de juros) \n')

escolha = int(input('Escolha Aqui: \n'))

if escolha == 1:

    print('Você Escolheu À Vista dinheiro/cheque (10% de desconto): ')
    total = preco - (preco * 0.10)
    print(f'O Total a Pagar Será: R${total}')

elif escolha == 2:

    print('Você Escolheu À Vista no cartão (5% de desconto): ')
    total = preco - (preco * 0.05)
    print(f'O Total a Pagar Será: R${total}')

elif escolha == 3:

    print('Você Escolheu Em até 2x no cartão (preço normal): ')
    total = preco
    parcela = total / 2
    print(f'Sua Compra Será Parcelada em (2)x de R${parcela:.2f} no Cartão e o Total será R${total:.2f} no Final sem Juros!')

elif escolha == 4:

    print('Você Escolheu Em até 3x no cartão (20% de juros): ')
    total = preco + (preco * 0.20)

    totalparc = int(input('Quantas Parcelas? '))
    parcelas = total / totalparc

    print(f'Sua Compra Será Parcelada em ({totalparc:.2f})x de R${parcelas:.2f} com Juros')
    print(f'O Total a Pagar Será: R${total:.2f}')

else:
    print('Escolha Inválida!!! Tente Novamente!!!')
