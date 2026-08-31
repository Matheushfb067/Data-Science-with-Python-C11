'''
Baseado nos commandos que vimos até o momento e no Dataset
fornecido, crie scripts em Python que respondam às seguintes
perguntas:

1. Apresente a porcentagem de missões que deram certo.

2. Qual é a média de gastos de uma missão espacial, considerando apenas as
   missões que possuem valores disponíveis (maiores que zero)?

3. Encontre quantas missões espaciais deste dataset foram realizadas pelos
   Estados Unidos (EUA).

4. Encontre a missão mais cara realizada pela empresa "SpaceX".

5. Mostre os nomes das empresas que já realizaram missões espaciais,
   juntamente com suas respectivas quantidades de missões. Use um laço for
   ao final para exibir as informações.

'''

import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype = 'str')

# 1. Apresente a porcentagem de missões que deram certo.
status_missoes = dataset[1:, 7]
quantidade_sucesso = np.sum(status_missoes == 'Success')
porcentagem = (quantidade_sucesso / len(status_missoes)) * 100
print(f'{porcentagem:.2f}')

# 2. 
gastos = dataset[1:, 6].astype(float)
gastos_validos = gastos[gastos > 0]
media_gastos = np.mean(gastos_validos)
print(f'{media_gastos:.2f}')

# 3. 
locais = dataset[1:, 2]
missoes_eua = np.char.find(locais, 'USA') >= 0 
quantidade_missoes_eua = np.sum(missoes_eua)
print(quantidade_missoes_eua)

# 4. 
companhia = dataset[1:, 1]
custo = dataset[1:, 6].astype(float)
detalhes = dataset[1:, 4]

filtro_spacex = np.char.find(companhia, 'SpaceX') >= 0
custo_spacex = custo[filtro_spacex] # custos exclusivos de missões da SpaceX
indice_maior_custo = custo_spacex.argmax()
detalhes_spacex = detalhes[filtro_spacex] # detalhes exclusivos de missões da SpaceX
missao_maior_custo = detalhes_spacex[indice_maior_custo]
print(missao_maior_custo)

# 5. 
nome_empresas = dataset[1:, 1]
empresas_unicas, quantidades = np.unique(nome_empresas, return_counts=True) #array de empresas que realizaram missõese de quantidades de missões

for i in range(len(empresas_unicas)): 
    print(empresas_unicas[i], quantidades[i])