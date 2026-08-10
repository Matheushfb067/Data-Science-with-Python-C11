# Estruturando uma matriz com contas:

import numpy as np

mtz = np.arange(10, 96, 5) # Cria uma lista de 10 a 95 pulando de 5 em 5
# print(mtz.reshape(3, 6)) # Reestrutura a lista para uma matriz de 3 linhas e 6 colunas
mtz = mtz.reshape(3, 6)
print(mtz)

# Extraindo a soma da primeira coluna
print(mtz.sum(axis = 0)) # Soma os elementos de todas as colunas (Eixo 0 = coluna 0)

# Agora como queremos retornar a soma somente dos elementos da primeira coluna fazemos um slicing
print(mtz.sum(axis = 0)[0])

# Agora eu quero somar meus elementos da segunda linha, para isso trocamos o eixo para 1
print(mtz.sum(axis = 1)[1])