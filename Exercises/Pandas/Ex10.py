'''
2. Encontre o nome e a região do país que possui a maior população segundo este 
Dataset
'''

import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

maior_populacao = ds.nlargest(1, 'Population')
nome_maior_populacao = maior_populacao[['Country', 'Region']]
print(nome_maior_populacao)