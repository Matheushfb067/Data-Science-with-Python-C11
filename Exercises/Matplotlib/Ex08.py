'''
8. Por meio do dataset space.csv, usando o conceito de subplot(), trace 
dois gráficos de barras separados lado a lado: à esquerda, as 5 empresas 
com mais missões de sucesso; à direita, as 5 empresas com mais missões 
de falha.
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('space.csv', sep = ';')

missoes_sucesso = ds[ds['Status Mission'] == 'Success']
missoes_falha = ds[ds['Status Mission'] == 'Failure']

sucesso_por_empresa = missoes_sucesso.groupby('Company Name').count()['Status Mission']
falha_por_empresa = missoes_falha.groupby('Company Name').count()['Status Mission']

cinco_sucesso = sucesso_por_empresa.nlargest(5)
cinco_falha = falha_por_empresa.nlargest(5)

plt.subplot(1, 2, 1)
plt.bar(cinco_sucesso.index, cinco_sucesso)
plt.title('5 empresas com mais sucessos')
plt.xlabel('Empresa')
plt.ylabel('Missões de sucesso')

plt.subplot(1, 2, 2)
plt.bar(cinco_falha.index, cinco_falha)
plt.title('5 empresas com mais falhas')
plt.xlabel('Empresa')
plt.ylabel('Missões de falha')

plt.show()
