'''
7. Utilizando do mesmo DataFrame, apresente a média dos elementos da
linha D usando a função loc() como base e a soma dos elementos da linha E
usando a função iloc() como base;
'''

import pandas as pd
import numpy as np

# plantando semente aleatoria
np.random.seed(10)

# Lista de Labels(Colunas)
colunas = ['W', 'X', 'Y', 'Z'] 
# Lista de Labels(Linhas)
linhas = ['A', 'B', 'C', 'D', 'E']
# Lista de Valores
valores = np.random.randint(1, 50, [5, 4])

df = pd.DataFrame(columns=colunas, index=linhas, data=valores)
print(df)
print("")

linhaD = df.loc[['D'], ['W', 'X', 'Y', 'Z']]
linhaE = df.iloc[4, :]

mediaLinhaD = np.mean(linhaD)
somaLinhaE = np.sum(linhaE)

print(f"A media dos elementos da linha D é: {mediaLinhaD}")
print(f"A Soma dos elementos da linha E é: {somaLinhaE}")