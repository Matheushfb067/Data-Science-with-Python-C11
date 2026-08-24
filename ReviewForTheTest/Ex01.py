'''
Questão 1
Faça um slicing no dataset para mostrar apenas o País (Country), Região 
(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos 
nele;
'''

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter = ';', dtype = 'str')
print(dataset)

print("")

country = dataset[0:, 0:4]
print(country)

print("")

'''
Questão 2
Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo 
este dataset;
'''

regioes = dataset[1:, 1]
regioes_unicas = np.unique(regioes)

print(f"Qauntidade de Regioes: {len(regioes_unicas)}")
print(f"Regioes: {regioes_unicas}")

print("")

'''
Questão 3
Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo 
este dataset
'''

alfabetizacao = dataset[1:, 9].astype(float)
soma = np.sum(alfabetizacao)
media = soma / len(alfabetizacao)
print(f'A média é: {media:.2f}')

print("")

'''
Questão 4
Conte quantos países são da América do Norte (NORTHERN AMERICA) 
segundo este dataset;
'''

regioes_paises = dataset[1:, 1]
paises_america_norte = np.char.find(regioes_paises, 'NORTHERN AMERICA') >= 0
quantidade_paises_america_norte = np.sum(paises_america_norte)
print(f'A qauntidade de paises da america do norte é: {quantidade_paises_america_norte}')

print("")

'''
Questão 5
Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) 
possui a maior renda per capita (GDP ($ per capita));
'''

regioes_america_carib = dataset[1:, 1]
paises = dataset[1:, 0]
rendas = dataset[1:, 8].astype(float)

# True: o país pertence à América Latina e ao Caribe; False: o país pertence a outra região.
mascara_regiao = np.char.find(regioes_america_carib, 'LATIN AMER. & CARIB') >= 0 # array composto por True e False

paises_filtrados = paises[mascara_regiao]
rendas_filtradas = rendas[mascara_regiao]

maior_renda = np.max(rendas_filtradas)
pais_maior_renda = paises_filtrados[rendas_filtradas == maior_renda]

print(pais_maior_renda)