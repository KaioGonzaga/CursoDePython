import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx')

#Values count
transacoes_loja = tabela_vendas['ID Loja'].value_counts()
#print(transacoes_loja)

#Groyp by
faturamento_produto = tabela_vendas.groupby('Produto').sum()
print(faturamento_produto)

faturamento_produto = tabela_vendas[['Produto', 'Valor Final']].groupby('Produto').sum()
print(faturamento_produto)