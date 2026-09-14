import pandas as pd
import numpy as np

# Carregando datassets com pandas:
# ds = np.loadtxt('paises.csv', delimiter=';', dtype='str') -> numpy 
ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print("")

# Slicing das colunas do datasset 
print(ds.columns)
print("")

# Slicing das 5 primeiras linhas do datasset (topo)
print(ds.head(5))
print("")

# Slicing das 3 ultimas linhas do datasset (base)
print(ds.tail(3))
print("")