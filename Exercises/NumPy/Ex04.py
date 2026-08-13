'''
4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas, multiplique
-os, e diga se esta matriz poderia se tornar um vetor unidimensional com número par ou ímpar 
de elementos 
'''

import numpy as np

mtz = np.array([ [1, 2, 3], [6, 5, 4], [7, 8, 9], [12, 11, 10] ])

linha, coluna = mtz.shape
print(f'Nunero de Linhas e colunas da matriz: {mtz.shape}')

total = linha * coluna
print(total)

if total % 2 == 0: 
    print('A matriz pode se tornar um vetor unidimensional com um numero PAR de elementos')
else: 
    print('A matriz pode se tornar um vetor unidimensional com um numero IMPAR de elementos')

vetor = mtz.reshape(-1)
print(vetor)