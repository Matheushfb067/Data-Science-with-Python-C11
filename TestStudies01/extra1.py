'''
Questão 1
Faça um slicing no dataset para mostrar apenas o País (Country), Região 
(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos 
nele;
'''

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

slicing = dataset[1:, 0:4]
print(slicing)

print("")

'''
Questão 2
Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo 
este dataset;
'''

regioes = dataset[1:, 1]
regioes_unicas = np.unique(regioes)

print(f'Quantidade de regioes: {len(regioes)}')
print(f'Diferentes regioes: {regioes_unicas}')

print("")

'''
Questão 3
Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo 
este dataset
'''

alfabetizacao = dataset[1:, 9].astype(float)
quantidade = np.sum(alfabetizacao)
taxa_media = quantidade / len(alfabetizacao)
print(f'{taxa_media:.2f}')

print("")

'''
Questão 4
Conte quantos países são da América do Norte (NORTHERN AMERICA) 
segundo este dataset;
'''

paises = dataset[1:, 1]
paises_america_norte = np.char.find(paises, 'NORTHERN AMERICA') >= 0
contagem_paises = np.sum(paises_america_norte)
print(contagem_paises)

print("")

'''
Questão 5
Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) 
possui a maior renda per capita (GDP ($ per capita));
'''

paises_ams = dataset[1:, 0]
regiao = dataset[1:, 1]
renda_gdp = dataset[1:, 8].astype(float)

mascara = np.char.find(regiao, 'LATIN AMER. & CARIB') >= 0

paises_filtrados = paises_ams[mascara]
gdp_filtrado = renda_gdp[mascara]

maior_renda = np.argmax(gdp_filtrado)

pais_maior_renda = paises_filtrados[maior_renda]

print(pais_maior_renda)