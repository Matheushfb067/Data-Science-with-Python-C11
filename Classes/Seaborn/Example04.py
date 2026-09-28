import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

''' Grafico Regplot - mostra a tendencia dos dados de um grafico por meio de uma regressão (linha), 
mostra também o intervalo de incerteza dos valores '''

ds_tips = sns.load_dataset('tips')
# print(ds_tips)

# Setando um estilo diferente no grafico
sns.set_style('dark')

# Setando uma fonte maior
sns.set_context('notebook')

sns.regplot(
    data = ds_tips,
    x = 'total_bill',
    y = 'tip',
    line_kws = {'color': 'red'} # cor da linha
)
plt.show()