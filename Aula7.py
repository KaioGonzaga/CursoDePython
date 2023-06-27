import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx')

tabela_gerentes = pd.read_excel('Gerentes.xlsx')

tabela_vendas = tabela_vendas.merge(tabela_gerentes)
print(tabela_vendas)