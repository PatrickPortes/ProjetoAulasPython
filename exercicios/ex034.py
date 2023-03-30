# Aumentos Múltiplos

sal = float(input('Digite o Valor do seu Salário: '))

if sal >= 1250.0:
    aum10 = sal + (sal * 0.10)
    #aum10 = sal + (sal * 10 / 100)
    print(f'Seu Salário de R${sal} receberá um aumento de 10%, você receberá {aum10} ')
else:
    aum15 = sal + (sal * 0.15)
    #aum15 = sal + (sal * 15 / 100)
    print(f'Seu Salário de R${sal} receberá um aumento de 15%, você receberá {aum15} ')