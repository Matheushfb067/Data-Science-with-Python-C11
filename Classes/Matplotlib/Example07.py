import matplotlib.pyplot as plt
import pandas as pd

# Lendo o dataset de paises
dfPaises = pd.read_csv('paises.csv', sep=';')

''' Um grafico de Torta (Pie Plot) é uma ferramenta eficaz para representar distribuições percentuais 
de maneira visual. O tamanho de cada fatia é a proporção de cada categoria no conjunto de dados '''

# Extraindo os países que não tem costa marítma
dfPaises_no_coast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]

# Extraindo a quantidade de paises que não tem costa maritima
qtdPaises_no_coast = len(dfPaises_no_coast)

# Extraindo a quantidade de paises que tem costa maritima
qtdPaises_coast = len(dfPaises) - qtdPaises_no_coast

# Traçando o grafico de tortas:
# autopct='%1.1f%%' é um formato usado no plt.pie() para mostrar a porcentagem em cada fatia do gráfico.
plt.pie(x = [qtdPaises_coast, qtdPaises_no_coast], labels = ['% Países com Costa', '% Países sem Costa'], autopct = '%1.1f%%') 
plt.show()