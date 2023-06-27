produtos = ['ABC123', 'abc12', ' ABC4578', 'ab8222']

texto = ' abddsdsc848'

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto


#texto = tratar_texto(texto)
print(tratar_texto(texto))

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)