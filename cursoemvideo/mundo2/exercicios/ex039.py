# Alistamento Militar

from datetime import date

atual = date.today().year

nasc = int(input('Qual o seu Ano de Nascimento? '))

idade = atual - nasc

print(f'Quem Nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o Alistamento!')
    ano = atual + saldo
    print('Seu Alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print(f'Você já realizou ou deveria ter realizado o alistamento há {saldo} anos!')
    ano = atual - saldo
    print('Seu Alistamento foi em {}'.format(ano))


''' MANEIRA QUE EU FIZ SEM IMPORT
ano = int(input('Qual o seu Ano de Nascimento? '))

if (ano + 18) < 2023:
    print('Ja Fazem {} Anos que Passou do Tempo do seu Alistamento!'.format(2023-(ano+18)))
elif (ano + 18) > 2023:
    print('Daqui {} Anos Quando Você Fizer 18 anos, Terá que Comparecer ao Alistamento!'.format((ano+18)-2023))
elif (ano + 18) == 2023:
    print('É Hora de Você Comparecer ao Alistamento!')
'''