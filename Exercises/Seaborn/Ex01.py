'''
1. Utilizando o dataset Iris do Seaborn, para os dados apenas da espécie ‘setosa’, 
avalie a correlação entre suas variáveis numéricas, apresentando os valores das 
correlações e permitindo identificar quais variáveis estão mais correlacionadas;
'''

import matplotlib.pyplot as plt
import seaborn as sns

ds_iris = sns.load_dataset('iris')
print(ds_iris)

# Filtrando apenas flores setosa
ds_setosa = ds_iris[ds_iris['species'] == 'setosa']

variaveis = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

corr = ds_setosa[variaveis].corr()

print(f'Correlação entre as variaveis da especie setosa: \n {corr.round(2)}')