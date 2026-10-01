'''
4. Utilizando o dataset space.csv, trace um gráfico em barras com as 
5 empresas que mais tiveram missões com status “Failure”.
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('space.csv', sep = ';')

missoes_falhas = ds[ds['Status Mission'] == 'Failure']
missoes_por_empresa = missoes_falhas.groupby('Company Name').count()['Status Mission']
cinco_empresas = missoes_por_empresa.nlargest(5)

plt.bar(cinco_empresas.index, cinco_empresas)
plt.xlabel('Empresa')
plt.ylabel('Quantidade de missões com falha')
plt.show()
