# Radar Eletrônico

vel = float(input('Qual a Velocidade do Carro em Km/h? '))

multa = (vel-80) * 7.0

if vel > 80.0:
    print(f'Você Ultrapassou o Limite de 80Km/h e Será Multado no Valor de R${multa}!!!')
else:
    print('Parabéns, Você Não Ultrapassou o Limite de Velocidade!!!')






