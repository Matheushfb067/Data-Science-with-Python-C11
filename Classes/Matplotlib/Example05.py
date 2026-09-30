import matplotlib.pyplot as plt
import pandas as pd

''' Um grafico de Dispersão (Scatter Plot) é util detectar outliers e padrões,
além de ser útil para se explorar a relação entre duas variáveis '''

# Lendo o dataset de paises
dfPaises = pd.read_csv('paises.csv', sep=';')

# Extraindo dados somente dos 6 maiores paises do mundo 
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')

# Plotando quais desses paises possui maior renda per capta 
# Observe que o tamanho de cada ponto ilustra o tamanho dos paises 
plt.scatter(dfPaises2['Country'], dfPaises2['GDP ($ per capita)'], s = dfPaises2['Area (sq. mi.)']/10000)
plt.show()