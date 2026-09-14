import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print("")

# Fazendo slicing no datasset:

# Para isso podemos somente passar as labels, ao em vez de picotar em valores numericos como no numpy
print(ds.columns)
print(ds[['Region', 'Climate', 'Service']])
print("")
