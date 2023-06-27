import pandas as pd


tabela_vendas = pd.read_excel('Vendas.xlsx')

#print(tabela_vendas)

#A partir de uma oluna que existe
tabela_vendas['Comissão'] = tabela_vendas['Valor Final'] * 0.05
print(tabela_vendas)


#Criar uma coluna com o valor padrão
tabela_vendas['Imposto'] = 0
print(tabela_vendas)

# Preencher todas as linha com o valor 0
tabela_vendas.loc[:,'Imposto'] = 0
print(tabela_vendas)

# TABELA DE VENDAS DE DEZEMBRO
tabela_dez = pd.read_excel('Vendas - Dez.xlsx')
print(tabela_dez)

tabela_vendas = tabela_vendas.append(tabela_dez)
print(tabela_vendas)


#Excluir a coluna
tabela_vendas = tabela_vendas.drop('Imposto', axis=0)

#Deletar linhas e colunas completamente vazias
tabela_vendas = tabela_vendas.dropna(how='all', axis=1)

#deletar linhas que possuem pelo menos 1 valor vazio
tabela_vendas = tabela_vendas.dropna()