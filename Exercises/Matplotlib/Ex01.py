''' 1. Por meio do dataset paises.csv, trace dois gráficos de linhas em 
um mesmo plano cartesiano, um mostrando a taxa de mortalidade 
(Deathrate) e outro a taxa de natalidade (Birthrate) dos países da 
América do Norte; '''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')

america_norte = ds[ds['Region'].str.strip() == 'NORTHERN AMERICA']

plt.plot(america_norte['Country'], america_norte['Deathrate'], 'r-')
plt.plot(america_norte['Country'], america_norte['Birthrate'], 'b--')

plt.xlabel('Pais')
plt.ylabel('Taxa')

plt.show()