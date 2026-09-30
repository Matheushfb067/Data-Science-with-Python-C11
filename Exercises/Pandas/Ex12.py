'''
4. Busque o nome de todos os países do Dataset que não possuem costa 
marítima (Coastline (coast/area ratio) == 0) e guarde-os em um novo
arquivo chamado noCoast.csv;
'''

import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep = ';')
print(ds)
print()

costa_maritima = ds['Coastline (coast/area ratio)']
sem_costa = costa_maritima == 0

paises_sem_costa = ds.loc[sem_costa, 'Country'] # pegando o nome dos paises
print(paises_sem_costa)

# criando novo csv contendo a coluna noCoast
paises_sem_costa.to_csv('noCoast.csv')