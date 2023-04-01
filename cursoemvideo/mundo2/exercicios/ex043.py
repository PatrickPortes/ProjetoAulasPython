# Índice de Massa Corporal

peso = float(input('Qual o seu Peso? (Kg) '))

alt = float(input('Qual a sua Altura? '))

imc = peso / (alt ** 2)

print(f'O seu IMC é = {imc:.2f}')

if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Você está em Sobrepeso')
elif imc >=30 and imc < 40:
    print('Você está em Obesidade')
elif imc >= 40:
    print('Você está em Obesidade Mórbida')



