'''
8. Por meio do dataset space.csv, após filtrar apenas as missões com custo
conhecido (Cost > 0), trace um Boxplot comparando a distribuição do custo
das missões (Cost) entre foguetes com status “StatusActive” e “StatusRetired”, 
permitindo identificar mediana, dispersão e outliers de cada grupo. 
'''

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

ds_space = pd.read_csv('space.csv', sep = ';')
print(ds_space)

cost_not_null = ds_space[ds_space['Cost'] > 0]

sns.boxplot(
    data = cost_not_null,
    x = 'Status Rocket',
    y = 'Cost'
)
plt.show()