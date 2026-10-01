'''
6. Com base nos dados do dataset space.csv, trace um gráfico em torta 
ilustrando a porcentagem geral de foguetes com status “StatusActive” e 
“StatusRetired”, considerando todas as empresas
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('space.csv', sep = ';')

foguetes_ativos = ds[ds['Status Rocket'] == 'StatusActive']
foguetes_aposentados = ds[ds['Status Rocket'] == 'StatusRetired']

plt.pie(x = [len(foguetes_ativos), len(foguetes_aposentados)], labels = ['Ativos', 'Aposentados'], autopct = '%1.1f%%')
plt.show()
