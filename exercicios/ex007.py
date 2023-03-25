# Média Aritmética

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

ma = float((n1 + n2) / 2)

print('A sua média aritmética é: {:.1f}'.format(ma))

if ma >= 7.0:
    print('Parabens Você Foi Aprovado!!!')
else:
    print('Você Foi Reprovado!!!')