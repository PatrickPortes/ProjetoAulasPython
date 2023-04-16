# Validando Expressões Matemáticas

expr = str(input('Digite a Expressão Matemática: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua Expressão Está Válida!!!')
else:
    print('Sua Expressão Está Inválida!!!')