import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

''' Grafico de Boxplot - dedicado a mediana(numero do meio - ordenamos os valores, se for uma valor 
impor o valor da mediana será o central, caso seja par, a mediana será a media dos dois centrais), 
cada uma das partes do grafico correspondem a 25% deles '''

# todo datasset do seaborn são datasets do pandas

ds_tips = sns.load_dataset('tips')
# print(ds_tips)

# Setando um estilo diferente no grafico
sns.set_style('dark')

# Setando uma fonte maior
sns.set_context('notebook')

# traçando o boxplot
sns.boxplot(
    data = ds_tips,
    x = 'day',
    y = 'tip',
    hue = 'sex'
)
plt.show()