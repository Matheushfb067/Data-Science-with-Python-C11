'''
3. Por meio do dataset space.csv, trace um gráfico em torta 
ilustrando a porcentagem de missões da empresa Roscosmos que 
deram certo e que deram errado;
'''

import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('space.csv', sep = ';')

missoes_roscosmos = ds[ds['Company Name'] == 'Roscosmos']

missoes_sucesso = missoes_roscosmos[missoes_roscosmos['Status Mission'] == 'Success']
missoes_erro = missoes_roscosmos[missoes_roscosmos['Status Mission'] != 'Success']

plt.pie(x = [len(missoes_sucesso), len(missoes_erro)], labels = ['Sucesso', 'Erro'], autopct = '%1.1f%%')
plt.show()
