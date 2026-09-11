import pandas as pd
import numpy as np

# Slicing de dados no Dataframe com LOC - Location(Labels) e ILOC - Index Location(Indices Numericos)

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

# Pegando apenas a linha C usando a função LOC
print(df.loc[['C'], ['W', 'X', 'Y', 'Z']])
print("")

# Pegando multiplas linhas usando LOC
print(df.loc[['B', 'E'], ['W', 'X', 'Y', 'Z']])
print("")

# Pegando apenas o quadrado do lado inferior direito da matriz valores: 37, 17, 12, 25
print(df.loc[['D', 'E'], ['Y', 'Z']])
print("")

# FAZENDO OS MESMOS EXEMPLOS ANTERIORES USANDO O ILOC

# Pegando apenas a linha C usando a função ILOC
print(df.iloc[2, :]) 
print("")

# Pegando multiplas linhas usando ILOC
print(df.iloc[[1, 4], :])
print("")

# Pegando apenas o quadrado do lado inferior direito da matriz valores: 37, 17, 12, 25 usando ILOC
print(df.iloc[[3, 4], [2, 3]])