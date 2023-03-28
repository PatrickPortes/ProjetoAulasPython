# Procurando uma String dentro de outra:

name = input('Digite o seu Nome Completo: ').strip()

print('Seu Nome tem Silva? {}'.format('silva' in name.lower()))