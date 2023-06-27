import pandas as pd


#dataframe = pd.dataframe()

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
          'qtde': [50, 70] 
        } 
tabela_vendas = pd.DataFrame(venda)

print(tabela_vendas)

tabela_vendas = pd.read_excel('Vendas.xlsx')

##print(tabela_vendas.describe())
##print(tabela_vendas.head())
##print(tabela_vendas.shape)

produtos = tabela_vendas['Produto']
##print(produtos)


#Pegar uma linha
print(tabela_vendas.loc[1:5])

# Pegar linhas que correspondem a uma condição
vendas_note_shopping_df = tabela_vendas.loc[tabela_vendas['ID_Loja'] == 'Norte Shopping']


# Pegar linhas que correnpondem a uma condição
print(tabela_vendas.loc[tabela_vendas['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']])

# Pegar um valor específico
print(tabela_vendas.loc[1, 'Produto'])


