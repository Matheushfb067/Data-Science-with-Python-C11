'''
7. Utilizando o dataset paises.csv, trace um Regplot relacionando a taxa de alfabetização 
(Literacy (%)) com a mortalidade infantil (Infant mortality (per 1000 births)), customizando 
a cor da linha de regressão;
'''

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

ds_paises = pd.read_csv('paises.csv', sep = ';')
print(ds_paises)

sns.regplot(
    data = ds_paises,
    x = 'Literacy (%)',
    y = 'Infant mortality (per 1000 births)',
    line_kws = {'color': 'red'}
)
plt.show()