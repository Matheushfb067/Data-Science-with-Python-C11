import pandas as pd
import numpy as np

# Como preencher um Dataframe:

# Lista de Labels(Colunas)
colunas = ['W', 'X', 'Y', 'Z']

# Lista de Labels(Linhas)
linhas = ['A', 'B', 'C', 'D', 'E']

np.random.seed(10)

# Lista de Valores
valores = np.random.randint(1, 50, [5, 4])

# DataFrame criado: 
df = pd.DataFrame(columns=colunas, index=linhas, data=valores)
print(df)
print("")

# Manipulando o Dataframe

# Puxando uma unica coluna do Dataframe
print(df['X'])
print("") 

# Puxando duas colunas do Dataframe
print(df[['Y', 'Z']])
print("")

# Puxando uma unica celula do Dataframe
# Primeiro a coluna e depois a linha
print(df['Y']['C'])
print("")

# Puxando multiplas colunas
print(df[['W', 'X', 'Z']])