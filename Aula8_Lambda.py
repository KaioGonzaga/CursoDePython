preco = 1000

def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(preco))


# Função Lambda
calcular_imposto2 = lambda x: x * 0.3

print(calcular_imposto2(preco))


#Função MAP

precos = [100, 500,10, 25]

impotos = list(map(lambda x: x*0.3,precos))
print(impotos) 