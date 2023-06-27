

lista_compras = ['carro', 'maça', 'laranja', 'banana']
print(lista_compras)

lista_compras.insert(1, 'chocolate')
print(lista_compras)

del lista_compras[4]
print(lista_compras)

lista_compras.remove('chocolate')
print(lista_compras)

lista_compras.append('carro')
print(lista_compras)

lista_sonhos = []

sonho = lista_compras.pop(-1)
print(sonho)

tarefas = []
tarefa = input('Insira uma tarefa')
tarefas.append(tarefa)

while tarefa !='':
    tarefa = input('Insira uma tarefa')
    tarefas.append(tarefa)