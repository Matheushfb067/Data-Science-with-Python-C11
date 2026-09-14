import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', sep=';')
print(ds)
print("")

# Criação e Aplicação de Funções Customizadas com Pandas: 

# Criando uma função em python para dar 10% de desconto em algo
def tenPercent(x):
    return x * 0.9

# Supondo que a taxa de mortalidade de todos os paises caiu em 10%

# Buscando coluna de taxa de mortalidade 
print(ds.columns)
print("")

deathrate = ds['Deathrate']
print(deathrate)

ds['Deathrate -10%'] = deathrate.apply(tenPercent) # Adicionando a coluna 'Deathrate -10%' no dataset
print(ds.head(2)) # vendo apenas as duas primeira linhas do dataset