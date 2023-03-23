#Dissecando uma Variável

x = input("Digite Alguma Coisa: ")

print("O tipo primitivo desse valor é: {}".format(type(x)))
print("O valor digitado é alpha numérico: ", x.isalnum())
print("O valor digitado é numérico: ", x.isnumeric())
print("O valor digitado é alfabético: ", x.isalpha())
print("O valor digitado tem espaço: ", x.isspace())
print("O valor digitado está em maiúsculo: ", x.isupper())
print("O valor digitado está em minúsculo: ", x.islower())
print("O valor digitado está capitalizada: ", x.istitle())
