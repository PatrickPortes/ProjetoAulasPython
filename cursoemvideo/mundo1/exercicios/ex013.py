# Reajuste Salarial

sal = float(input('Qual seu salário atual? R$ '))

reaj = float(sal + sal *0.15)

#Poderia ser tbm
# reaj = sal + (sal * 15 / 100)

print(f'Seu novo salário com 15% de aumento é: {reaj:.2f}')