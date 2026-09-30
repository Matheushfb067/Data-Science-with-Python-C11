'''
6. Agrupe os países por região e mostre as estatísticas descritivas 
da coluna Population de cada região. Em seguida, mostre apenas as
5 primeiras linhas deste resultado;
'''

import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

regiao = ds.groupby('Region')
estatisticas = regiao['Population'].describe()
print(estatisticas.head(5))