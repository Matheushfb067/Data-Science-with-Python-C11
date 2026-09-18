'''
6. Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
média dos elementos da coluna X que são menores que 30;
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

colunaX = df['X']
colunaXMenores30 = colunaX[colunaX < 30]

mediaColunaX = np.mean(colunaXMenores30)
print(f'A média dos elementos da coluna x é: {mediaColunaX:.2f}')