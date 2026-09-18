'''
8. Faça um Slicing na matriz mostrando apenas as linhas A, C e E
juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
elementos de cada uma destas linhas e cada uma destas colunas.
'''

import pandas as pd
import numpy as np

# plantando semente aleatória
np.random.seed(10)
# Lista de Labels (Colunas)
colunas = ['W', 'X', 'Y', 'Z'] 
# Lista de Labels (Linhas)
linhas = ['A', 'B', 'C', 'D', 'E']
# Lista de Valores
valores = np.random.randint(1, 50, [5, 4])

df = pd.DataFrame(columns=colunas, index=linhas, data=valores)
print(df)
print("")

slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print("Slicing:")
print(slicing)

somaLinhas = slicing.sum(axis=1)
somaColunas = slicing.sum(axis=0)

print(f"Soma de cada linha: {somaLinhas}")

print(f"Soma de cada coluna: {somaColunas}")