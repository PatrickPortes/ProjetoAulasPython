# Tratando Vários Valores v1.0

num = cont = soma = 0

num = float(input('Digite o Número [999 para Parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = float(input('Digite o Número [999 para Parar]: '))

print(f'VOCÊ DIGITOU {cont} NÚMEROS, E A SOMA ENTRE ELES FOI {soma}!!!')
# Para ignorar o 999 poderia ser feito tbm (cont -1, soma -999)
