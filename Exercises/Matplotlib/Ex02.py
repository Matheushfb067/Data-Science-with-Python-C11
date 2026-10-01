''' 
2. Por meio do dataset space.csv, trace um gráfico em barras 
mostrando quantas empresas espaciais diferentes os EUA e a CHINA 
possuem;
Dica: não se esqueça de retirar os resultados repetidos
'''

import matplotlib.pyplot as plt
import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')

locais = dataset[1:, 2]
empresas = dataset[1:, 1]

missoes_eua = np.char.find(locais, 'USA') >= 0
missoes_china = np.char.find(locais, 'China') >= 0

empresas_eua = np.unique(empresas[missoes_eua])
empresas_china = np.unique(empresas[missoes_china])

nomes_paises = np.array(['EUA', 'CHINA'])
quantidade_empresas = np.array([len(empresas_eua), len(empresas_china)])

plt.bar(nomes_paises, quantidade_empresas)
plt.xlabel('País')
plt.ylabel('Quantidade de empresas')
plt.show()  
