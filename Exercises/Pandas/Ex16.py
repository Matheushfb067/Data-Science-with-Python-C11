'''
8. Remova a coluna Coastline(coast/area Ratio) do dataset. Em seguida, salve 
este novo dataset em um arquivo chamado paises_sem_coastline.csv.
'''

import pandas as pd 
import numpy as np 

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print()

ds_sem_coastline = ds.drop(columns=['Coastline (coast/area ratio)'])
ds_sem_coastline.to_csv('paises_sem_coastline.csv', sep=';', index=False)