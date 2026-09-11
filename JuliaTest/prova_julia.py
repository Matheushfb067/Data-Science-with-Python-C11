'''
Questão 1: 
Qual a média de preço de um chocolate ao leite segundo este dataset?
'''

import numpy as np
dataset = np.loadtxt('chocolate_sales_2025.csv', delimiter=',', dtype='str')

chocolate_tipo = dataset[1:, 3]
preco_chocolate = dataset[1:, 7].astype(float)

chocolate_ao_leite_mascara = np.char.find(chocolate_tipo, 'Milk Chocolate') >= 0
chocolate_ao_leite_preco = preco_chocolate[chocolate_ao_leite_mascara]

media_preco_chocolate_leite = np.mean(chocolate_ao_leite_preco)

print(f'A média é: US$ {media_preco_chocolate_leite:.2f}')

'''
Questão 2:
Qual o país com maior número de registros de chocolates neste dataset?
'''

paises = dataset[1:, 4]

# cria um vetor com os paises sem repetição - conta quantas vezes os paises se repetem 
paises_unicos, quantidade = np.unique(paises, return_counts=True)
indice_maior = quantidade.argmax()

print(f'O pais com o maior registro de chocolates é: {paises_unicos[indice_maior]}')

'''
Questão 3:
5% de todas as vendas feitas com cartão de crédito vão para as operadoras de cartão.
Baseado nos dados deste dataset, quanto as operadoras de cartão faturaram?
'''

metodo_pagamento = dataset[1:, 6]
ravenue_usd = dataset[1:, 9].astype(float)

cartao_credito = np.char.find(metodo_pagamento, 'Card') >= 0

total = np.sum(ravenue_usd[cartao_credito]) * 0.05
print(f'As operadoras de cartão faturam: {total:.2f}')

'''
Questão 4:
Mostre o nome da marca de chocolates com maior número de registros (linhas) nos
supermercados deste dataset;
'''

marca = dataset[1:, 2]

marca_unica, contagem = np.unique(marca, return_counts=True)
indice_marca_maior = contagem.argmax()

print(f'A marca com maior numero de registros é: {marca_unica[indice_marca_maior]}')

'''
Questão 5:
Qual a quantidade total de unidades de chocolates vendidas segundo este dataset?
'''

quantia_vendida = dataset[1:, 8].astype(int)
total_vendas = np.sum(quantia_vendida)
print(f'A quantidade total de unidades vendidas é: {total_vendas}')
