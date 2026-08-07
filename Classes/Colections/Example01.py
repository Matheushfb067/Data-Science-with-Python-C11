# Tuples: 

nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan') # -> isso é a representação basica de uma coleção!
print(nomes)
print(type(nomes))

'''
-> TUPLAS SÃO IMUTAVEIS: 

# TENTANDO INSERIR UM ELEMENTO NA TUPLA
nomes[4] = 'Picolo' #-> isso não funciona 

# TENTANDO ALTERAR UM ELEMENTO DA TUPLA
nomes[0] = 'Majin Boo'
'''

# Slicing de Dados: 
print(nomes[1])
'''
 # sempre que fazemos um fateamento em python, o primeiro argumento é sempre inculusive e o 
 # segundo argumento é sempre exclusive, por isso o indice de 'Trunks', passa a ser 3, mesmo 
 # na tupla, seu indice inclucive, seja 2!
'''
print(nomes[1:3])
print(nomes[1:]) # -> pega do indice indicado em diante

# O python também trabalha com indices negativos
print(nomes[-2]) # -> varre de tras para frente na tupla/vetor