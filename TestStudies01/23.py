'''
Baseado nos comandos que vimos até o momento e no Dataset fornecido,
crie scripts em Python que respondam às seguintes perguntas:

6. Qual a porcentagem de missões realizadas com foguetes cujo status é
   "StatusRetired" (coluna Status Rocket)?

7. Quantas missões foram lançadas a partir de localizações que contêm
   "Russia" (coluna Location)?

8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.

'''

import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str')

# 6.
coluna_status_rocket = dataset[1:, 5]
mascara = coluna_status_rocket == 'StatusRetired'

quantos_aposentados = np.sum(mascara)
porcentagem = (quantos_aposentados / len(coluna_status_rocket)) * 100

print(f'{porcentagem:.2f}')

# 7,
coluna_location = dataset[1:, 2]
missoes_russia = np.char.find(coluna_location, 'Russia') >= 0
quantidade_missies_russia = np.sum(missoes_russia)
print(quantidade_missies_russia)

# 8.
custo = dataset[1:, 6].astype(float)
empresa = dataset[1:, 1]

indice_maior_custo = custo.argmax()
filtro_custo = custo[indice_maior_custo]
filtro_empresa = empresa[indice_maior_custo]

print(filtro_custo, filtro_empresa)