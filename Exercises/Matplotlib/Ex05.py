'''
5. Por meio do dataset paises.csv, trace um gráfico de dispersão 
relacionando a renda per capita (GDP ($ per capita)) com a taxa de 
alfabetização (Literacy (%)) dos países da América Latina. Além disso,
faça com que o tamanho de cada ponto represente a população do país;
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')

america_latina = ds[ds['Region'].str.strip() == 'LATIN AMER. & CARIB']

plt.scatter(america_latina['GDP ($ per capita)'], america_latina['Literacy (%)'], s = america_latina['Population'] / 10000)
plt.xlabel('Renda per capita (GDP)')
plt.ylabel('Taxa de alfabetização (%)')
plt.show()
