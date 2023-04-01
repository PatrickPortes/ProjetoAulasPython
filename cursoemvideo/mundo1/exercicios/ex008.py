# Conversor de Medidas:

m = float(input('Digite um valor em metros: '))

cm = float(m * 100)

mm = float(m * 1000)

print('Esse valor em metros convertido para centímetros é: {:.0f} cm \n'
      'e convertido para milímetros é: {:.0f} mm'.format(cm, mm))