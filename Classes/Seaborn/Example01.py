import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

# Importando o dataset tips - iterno do seaborn
ds_tips = sns.load_dataset('tips')
# print(ds_tips)

# Setando um estilo diferente no grafico
sns.set_style('dark')

# Setando uma fonte maior
sns.set_context('talk')

# Traçando o scatterplot
sns.scatterplot(data = ds_tips, x = 'total_bill', y = 'tip')
plt.xlabel('Conta total em US$')
plt.ylabel('Gorjeta em US$')
plt.show()