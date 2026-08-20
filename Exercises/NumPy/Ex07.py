'''
Baseado nos commandos que vimos até o momento e no Dataset fornecido, 
crie scripts em Python que respondam às seguintes perguntas:
    6. Qual a porcentagem de missões realizadas com foguetes cujo status é
    "StatusRetired" (coluna Status Rocket)?
    7. Quantas missões foram lançadas a partir de localizações que contêm
    "Russia" (coluna Location)?
    8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.
'''

import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str')
print(dataset)

print("")

# 6.
coluna_status_rocket = dataset[1:, 5] # Pegando coluna Status Rocket
quantidade = np.sum(coluna_status_rocket == 'StatusRetired')
porcentagem_status_retired = (quantidade / len(coluna_status_rocket)) * 100 
print(f'A porcentagem de missões com StatusRetired é: {porcentagem_status_retired:.2f}')

print("")

# 7.
coluna_location = dataset[1:, 2]
missoes_russia = np.char.find(coluna_location, 'Russia') != -1
quantidade_missoes_russia = np.sum(missoes_russia)
print(f'A quantidade de missões lançadas pela Russia foi: {quantidade_missoes_russia}')

print("")

# 8. 
empresas = dataset[1:, 1]
valor = dataset[1:, 6].astype(float)

valor_mais_caro  = valor[0]
indice_maior_custo = 0

for i in range(len(valor)):
    if valor[i] > valor_mais_caro:
        valor_mais_caro = valor[i]
        indice_maior_custo = i

empresa_mais_cara = empresas[indice_maior_custo]
print(f"A missão mais cara do Dataset foi realizada por: {empresa_mais_cara}")
