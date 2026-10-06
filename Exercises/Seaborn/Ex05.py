'''
5. Utilizando o dataset paises.csv, calcule a correlação entre “GDP ($ per capita)”, 
“Literacy (%)”, “Infant mortality (per 1000 births)” e “Phones (per 1000)”, apresentando 
o resultado em um Heatmap com os valores numéricos exibidos;
'''

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

ds_paises = pd.read_csv('paises.csv', sep = ';')
print(ds_paises)

corr = ds_paises[['GDP ($ per capita)', 'Literacy (%)', 'Infant mortality (per 1000 births)', 'Phones (per 1000)']].corr()

sns.heatmap(
    data = corr,
    annot = True,
    fmt = '.2f'
)
plt.show()