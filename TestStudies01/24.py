'''
Questão 1
Faça um slicing no dataset para mostrar apenas o País (Country), Região 
(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos 
nele;
'''

import numpy as np
dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

slicing = dataset[1:, 0:4]
print(f'{slicing}')

print("")

'''
Questão 2
Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo 
este dataset;
'''

regioes = dataset[1:, 1]
diferentes_regioes = np.unique(regioes)

print(f'Quantidade de regiões: {len(regioes)}')
print(f'Diferentes regiões: {diferentes_regioes}')

print("")


'''
Questão 3
Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo 
este dataset
'''

alfabetizaçao = dataset[1:, 9].astype(float)
soma_alfabetizacao = np.sum(alfabetizaçao)
media_alfabetizacao = soma_alfabetizacao / len(alfabetizaçao)
print(f'A média de alfabetização é: {media_alfabetizacao}')

print("")

'''
Questão 4
Conte quantos países são da América do Norte (NORTHERN AMERICA) 
segundo este dataset;
'''

coluna_regioes = dataset[1:, 1]
paises_america_norte = np.char.find(coluna_regioes, 'NORTHERN AMERICA') >= 0 
quantidade_paises_america_norte = np.sum(paises_america_norte)
print(f'A quantidade de paises da america do norte é: {quantidade_paises_america_norte}')

print("")

'''
Questão 5
Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) 
possui a maior renda per capita (GDP ($ per capita));
'''

regioes_coluna = dataset[1:, 1]
coluna_paises = dataset[1:, 0]
coluna_gpd = dataset[1:, 8].astype(float)

mascara = np.char.find(regioes, 'LATIN AMER. & CARIB') >= 0

paises_filtrados = coluna_paises[mascara]
gdp_filtrado = coluna_gpd[mascara]

maior_renda = np.argmax(gdp_filtrado)

pais_maior_renda = paises_filtrados[maior_renda]
print(f'O pais com a maior renda é: {pais_maior_renda}')