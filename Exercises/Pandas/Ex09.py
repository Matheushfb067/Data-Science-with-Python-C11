'''
1. Carregue o Dataset paises.csv e em seguida mostre:
a.Quais são os países da OCEANIA;
b.Quantos países são da OCEANIA;
Dica: para busca de padrões textuais no Pandas, use métodos da subclasse str da 
Series. Ex: series.str.contains(‘texto’)
'''

import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

regiao = ds['Region'] # Pegando a coluna região
oceania = regiao.str.contains('OCEANIA') # Buscando padrão OCEANIA dentro de regiao

paises_oceania = ds.loc[oceania, 'Country'] # Seleciona os paises da oceania
print(f'Os paises da Oceania são: \n {paises_oceania}')
print(f'A quantidade de países da Oceania é: {paises_oceania.count()}')