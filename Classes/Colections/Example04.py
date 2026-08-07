# Dicionarios

pessoa = {
    'nome': 'Goku',
    'idade': 52,
    'sexo': 'M', 
}
print(pessoa)
print(type(pessoa))

# CRUD:

#CREATE
pessoa['Desenho'] = 'Dragon Ball Z'
print(pessoa) 

# READ
print(pessoa['nome'])

# UPDATE
pessoa['Desenho'] = 'Dragon Ball GT'
print(pessoa)

# DELETE 
del pessoa['sexo']
print(pessoa)