faturamento = [10000, 300000, 148888, 3333, 11458]
print(faturamento)

lojas = ['Sao Pulo', 'Rio de Janeiro', 'Curitiba', 'Brasilia', 'Sao Vicente']

#Ordernar a lista em ordem crescente
faturamento.sort()
print(faturamento)

#Ordernar a lista em ordem decrescente
faturamento.sort(reverse=True)
print(faturamento)

resultados = []

#Criando conjunto chave/valor
for i in range(5):
    tuple = (lojas[i-1], faturamento[i-1])
    resultados.append(tuple)

print(resultados)
