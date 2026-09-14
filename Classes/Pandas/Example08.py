import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print("")

# Agrupamento de Dados (groupby - só funciona se o dataset tiver ao menos uma coluna com dados categorizados) 

# Agrupando paises por região (Contando o numero de paises por região):
group_region = ds.groupby('Region')
# O print(group_region) retorna um objeto e quando passamos o .count()['Country'] ai sim ele nos retornam as regioes e a quantia de paises
print(group_region.count()['Country'])
print("")

# Somando a população de cada região 
group_region = ds.groupby('Region')
print(group_region.sum()['Population']) 