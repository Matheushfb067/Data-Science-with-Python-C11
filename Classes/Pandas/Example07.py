import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print("")

# Criando Novos Arquivos com o Pandas: 

# Calculando a porcentagem da população de cada pais no mundo 

# Calculando população total do planeta
total_population = np.sum(ds['Population'])
print(total_population)

# Calculndo a porcetagem de cada pais
seriesPercentCountryes = (ds['Population'] / total_population) * 100 # Series por conta de ter uma unica dimensão (justificando nome da variavel)
print(seriesPercentCountryes)

# Adicionando esta series no Datasset
ds['% Population'] = np.round(seriesPercentCountryes, 3) # round arredonda para 3 casas decimais

# Criando novo Datasset com a nova coluna
ds.to_csv('paises_v2.csv')
print("")

# Usando condicional para pegar os 5 paises que mais tem gente (.nlargest)
print(ds.nlargest(5, '% Population')['Country']) # Já mostrando o noem dos paises junto com os maiores
print("")

# Usando condicional para pegar os 5 paises que menos tem gente (.nsmallest)
print(ds.nsmallest(5, '% Population')['Country'])
print("")