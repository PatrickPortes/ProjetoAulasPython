# Conversor de Bases Numéricas

num = int(input('Digite um Número Inteiro: '))

print('\nEscolha Qual Será a Base de Conversão: \n')

print('Digite 1 para Binário ')
print('Digite 2 para Octal ')
print('Digite 3 para Hexadecimal \n')

escolha = int(input('Escolha Aqui: '))

if escolha == 1:
    '''Binário'''
    print(f'O Número {num} convertido para binário é {bin(num)[2:]} ')
elif escolha == 2:
    '''Octal'''
    print(f'O Número {num} convertido para octal é {oct(num)[2:]} ')
elif escolha == 3:
    '''Hexadecimal'''
    print(f'O Número {num} convertido para hexadecimal é {hex(num)[2:]} ')
else:
    print('Escolha Inválida!! Tente Novamente!!')