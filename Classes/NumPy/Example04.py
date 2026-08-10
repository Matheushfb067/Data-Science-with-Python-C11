# Numeros Aleatorios em NumPy - Modulo  Random

import numpy as np

arr = np.random.randint(1, 10, 10) # cria numeros aleatorios de 1 a 9 
print(arr)

# Plantando a semente aleatoria de modo que manipula a memoria do computador para dar o mesmo resultado
np.random.seed(5)
print(arr)

# Extraindo elementos unicos
print(np.unique(arr)) # extrais apenas os elementos unicos (sem repetição)

# Contando quantos elementos unicos eu tenho dentro do array
print(np.unique(arr, return_counts=True)) # retorna quantas vezes cada elemento se repete em suas posições originais