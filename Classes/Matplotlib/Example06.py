import matplotlib.pyplot as plt
import pandas as pd

# Lendo o dataset de paises
dfPaises = pd.read_csv('paises.csv', sep=';')

''' Um Grafico de barras (Bar Plot) representa e compara dados quantitativos de forma visual
ele permite que se identifique rapidamente tendencias, padrões e diferenças entre os valores apresentados '''

# Extraindo 5 paises com o maior PIB per capta (GPD) do dataset
dfBiggestGPD = dfPaises.nlargest(5, 'GDP ($ per capita)')

# Pegando as Series dos paises e os valores de GPD separadamente 
dfBiggestGPD_country = dfBiggestGPD['Country']
dfBiggestGPD_gpd = dfBiggestGPD['GDP ($ per capita)']

# Traçando o grafico de barras para ilustrar as diferenças
plt.bar(dfBiggestGPD_country, dfBiggestGPD_gpd, color = 'blue')
plt.show()