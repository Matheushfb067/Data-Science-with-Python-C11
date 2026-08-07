# Misturando Coleções: 

pessoa1 = {'nome': 'Batman', 'cidade': 'Gotam'}
pessoa2 = {'nome': 'Jiraya', 'cidade': 'Konoha'}
pessoa3 = {'nome': 'Clark Kent', 'cidade': 'Crypton'}

alunos = [pessoa1, pessoa2, pessoa3] # Lista de dicionarios

# Apenas os dados do Jiraya
print(alunos[1])

# Apenas a cidade do Batman
print(alunos[0]['cidade'])

# Mostrar dados da pessoa 2 em diante
print(alunos[1:])