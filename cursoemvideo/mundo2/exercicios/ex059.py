# Criando um Menu de Opções

from time import sleep

print('='*23)
print(' REALIZANDO OPERAÇÕES:')
print('='*23)

n1 = float(input('\nDigite o Primeiro Valor: '))
n2 = float(input('Digite o Segundo Valor: '))

opcao = 0

while opcao != 5:

    print('\n======')
    print(' MENU:')
    print('=' * 6)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do Programa')

    opcao = int(input('\nSelecione uma Opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'\nA Soma de {n1:.0f} + {n2:.0f} = {soma:.1f}')
        sleep(3)

    elif opcao == 2:
        mult = n1 * n2
        print(f'\nA Multiplicação de {n1:.0f} X {n2:.0f} = {mult:.1f}')
        sleep(3)

    elif opcao == 3:
        if n1 > n2:
            print(f'\n{n1} é maior que {n2}!!!')
        elif n1 < n2:
            print(f'\n{n1} é menor que {n2}!!!')
        else:
            print(f'\n{n1} é igual a {n2}!!!')
        sleep(3)

    elif opcao == 4:
        print('\nDigite Novamente os Valores: ')
        n1 = float(input('\nDigite o Primeiro Valor: '))
        n2 = float(input('Digite o Segundo Valor: '))

    elif opcao == 5:
        print('FIM')

    else:
        print('\nOpção Inválida!!! ')
        print('Digite Novamente a Opção!!!')
        sleep(2)
