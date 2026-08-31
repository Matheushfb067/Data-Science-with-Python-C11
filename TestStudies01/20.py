'''
4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e
colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor
unidimensional com número par ou ímpar de elementos
'''

import numpy as np

mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtz)

linha, coluna = mtz.shape
print(f'Nunero de Linhas e colunas da matriz: {mtz.shape}')

total = linha * coluna

if total % 2 == 0: 
    print('A matriz pode se tornar um vetor unidimensional com um numero PAR de elementos')
else: 
    print('A matriz pode se tornar um vetor unidimensional com um numero IMPAR de elementos')

vetor = mtz.reshape(-1)
print(vetor)