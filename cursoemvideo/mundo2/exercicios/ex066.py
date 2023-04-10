# Vários Números com Flag

cont = soma = 0

while True:
    num = int(input('Digite um Número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Os Números Foram Digitados {cont} Vezes, e a Soma Deles é: {soma}')
