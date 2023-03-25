#Dobro, Triplo, Raiz Quadrada

x = int(input('Digite um número a sua escolha: '))

d = x * 2

t = x * 3

rq = x **(1/2)

print('O dobro desse número é: {} \n'
      'O triplo desse número é: {} \n'
      'A raiz quadrada desse número é: {:.2f} '
      .format(d, t, rq))