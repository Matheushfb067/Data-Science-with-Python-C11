'''
6. Com o dataset paises.csv, trace um Boxplot comparando a distribuição do 
“GDP ($ per capita)” entre os países da América Latina e da Europa Ocidental, 
permitindo assim identificar mediana, dispersão e outliers de cada grupo;
'''

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

ds_paises = pd.read_csv('paises.csv', sep = ';')
print(ds_paises)

regioes = ['LATIN AMER. & CARIB', 'WESTERN EUROPE']
paises_filtrados = ds_paises[ds_paises['Region'].str.strip().isin(regioes)]

sns.boxplot(
    data = paises_filtrados,
    x = 'Region',
    y = 'GDP ($ per capita)'
)
plt.show()