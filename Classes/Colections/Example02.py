# Lists: 

# Permite fazer tudo que não é possivel de fazer na tupla!

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(nomes)
print(type(nomes))

# CRUD de dados na lista
# CREATE 
nomes.append('Majin Boo') # -> add algo no final
nomes.insert(2, 'Picolo') # -> add na posição especifica e empurra os demais
print(nomes)

# READ
# mesmo procedimento da tupla

# Update
# -> Atualizando a lista
nomes[0] = 'Tenshin Han' 
print(nomes)

# DELETE
# -> Deleção por indice: 
del nomes[1] # Deletando o elemento da posição 1

# -> Deleção por valor: 
nomes.remove('Trunks')
print(nomes)