'''
Questão 1: 
Qual a média de preço de um chocolate ao leite segundo este dataset?
'''

import numpy as np
dataset = np.loadtxt('chocolate_sales_2025.csv', delimiter=',', dtype='str')

produto_tipo = dataset[1:, 3]
produto_preco = dataset[1:, 7].astype(float)

chocolate_ao_leite_mascara = np.char.find(produto_tipo, 'Milk Chocolate') >= 0
chocolate_ao_leite_preco = produto_preco[chocolate_ao_leite_mascara]
media_preco_chocolate_ao_leite = np.mean(chocolate_ao_leite_preco)
print(f'{media_preco_chocolate_ao_leite:.2f}')

'''
Questão 2:
Qual o país com maior número de registros de chocolates neste dataset?
'''

pais = dataset[1:, 4]
pais_contagem, quantidade = np.unique(pais, return_counts=True)
indice_maior = quantidade.argmax()

print(f'{pais_contagem[indice_maior]}')

'''
Questão 3:
5% de todas as vendas feitas com cartão de crédito vão para as operadoras de cartão.
Baseado nos dados deste dataset, quanto as operadoras de cartão faturaram?
'''

metodo_pagamento = dataset[1:, 6]
receita_usd = dataset[1:, 9].astype(float)
cartao_credito = np.char.find(metodo_pagamento, 'Card') >= 0
total = np.sum(receita_usd[cartao_credito]) * 0.05
print(f'{total:.2f}')

'''
Questão 4:
Mostre o nome da marca de chocolates com maior número de registros (linhas) nos
supermercados deste dataset;
'''

marca = dataset[1:, 2]
marca_unica, contagem = np.unique(marca, return_counts=True)
indice_marca_maior = contagem.argmax()
print(f'{marca_unica[indice_marca_maior]}')

'''
Questão 5:
Qual a quantidade total de unidades de chocolates vendidas segundo este dataset?
'''

unidades_vendidas = dataset[1:, 8].astype(int)
total_unidades = np.sum(unidades_vendidas)
print(f'{total_unidades}')