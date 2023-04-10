# Simulador de Caixa Eletrônico

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Qual o Valor de Saque? R$'))

total = valor
ced = 50
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} Cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break

print('='*30)
print('VOLTE SEMPRE AO NOSSO BANCO!!!')