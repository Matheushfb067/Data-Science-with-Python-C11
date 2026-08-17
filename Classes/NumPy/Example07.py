# Analise de padroes textuais com NumPy

import numpy as np

arr = np.array(['Inatel', 'Casa Viva', 'ICC', 'CDG', 'eHealth', 'CSILab', 'RobotBulls', 'ProdLab', 'CRA', 'CRR'])
print(arr)

# Submodulo do NumPy para trabalhar com textos: char
# Buscando qual texto aceita um padrão informado: 

'''
Retorna uma litsa de numeros positivos e negativos, todos os -1 são as palavras que não contem a, 
já os valores possitivos indicam a posição com a qual a letra aparece na palavra
'''
arr = np.char.upper(arr) # Jogando todo mundo para maiusculo

print(np.char.find(arr, 'A'))

# Retorna a mascara True e false
print(np.char.find(arr, 'A') >= 0)
cond = np.char.find(arr, 'A') >= 0
print(arr[cond])