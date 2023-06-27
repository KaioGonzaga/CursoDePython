
#DICIONÁRIO

email_gerentes = {
    'Iguatemi': 'iguatemi@gmail.com',
    'Plaza': 'plaza@gmail.com',
    'Barra': 'barra@gmail.com'
}

email = email_gerentes['Iguatemi']
print(email)

email_gerentes['Leblon'] = 'leblon@gmail.com'
print(email_gerentes)

#Laço FOR

for shopping in email_gerentes:
    print(shopping)


#Forma dicionario.key

print(email_gerentes.keys())


# Laço FOR para percoorrer valor

for shopping in email_gerentes:
    email = email_gerentes[shopping]
    print(email)

# Dicionario values

print(email_gerentes.values())

# Retirar uma chave/valor

email_gerentes.pop('Leblon')
print(email_gerentes)

#Verificar se existe u item dentro do dicionario

if 'Leblon' in email_gerentes:
    print('Existe')
else:
    print('Não existe')



if 'iguatemi@gmail.com' in email_gerentes.values():
    print('Existe')
else:
    print('Não existe')