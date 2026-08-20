'''
Baseado nos commandos que vimos até o momento e no Dataset fornecido, crie scripts em Python que 
respondam às seguintes perguntas:
1. Apresente a porcentagem de missões que deram certo
2. Qual a media de gastos de uma missão especial se baseando em missões
que possuam valores disponíveis (> 0)?
3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (EUA)
4. Encontre qual foi a missão mais cara realizada pela empresas “SpaceX”
5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas 
quantidades de missões (use o for no final para mostrar as informações)
'''

import numpy as np 

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')
print(dataset)

print("")

# 1.
status_missoes = dataset[1:, 7] # 1: - começe da linha de incdice 1 e vá até a ultima -> 7 - pegue somente a coluna de índice 7
quantidade_sucesso = np.sum(status_missoes == 'Success')
porcentagem = (quantidade_sucesso / len(status_missoes)) * 100 # len(status_missões) -> conta a quantidade total de missões
print(f"A porcentagem de missões que tiveram sucesso foi: {porcentagem:.2f}%")

print("")

# 2.
coluna_gastos = dataset[1:, 6].astype(float) # 1: - começe da linha de incdice 1 e vá até a ultima -> 6 - pegue somente a coluna de indice 6
gastos_validos = coluna_gastos[coluna_gastos > 0] # Guarda somente os custos maiores que 0
soma_gastos = np.sum(gastos_validos)
media_gastos = soma_gastos / len(gastos_validos)
print(f'A média dos gastos das missões espaciais é: {media_gastos:.2f}')

print('')

# 3. 
locais = dataset[1:, 2]
missoes_eua = np.char.find(locais, 'USA') != -1 # Me retorna um vetor com as posições de onde aparece usa e o != -1 elimina as posições onde não apareceu que também são mostradas
quantidade = np.sum(missoes_eua)
print(f'Quantidade de missões espaciais realizadas pelos EUA: {quantidade}')

print('')

# 4.
empresas = dataset[1:, 1]
nomes_missoes = dataset[1:, 4]  
custos = dataset[1:, 6].astype(float)

filtro_spacex = empresas == 'SpaceX'
custos_spacex = custos[filtro_spacex]
missoes_spacex = nomes_missoes[filtro_spacex]

indice_maior_custo = np.argmax(custos_spacex)
missao_mais_cara = missoes_spacex[indice_maior_custo]
print(f"A missão mais cara da SpaceX foi: {missao_mais_cara}")

print("")

# 5. 
empresas_unicas, quantidades = np.unique(empresas, return_counts=True)

for nome, qtd in zip(empresas_unicas, quantidades):
    print(f"{nome}: {qtd} missão(ões)")