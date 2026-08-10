# Operações entre Numpy Arrays

import numpy as np 

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([60, 40, 20, 10, 5])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)

# Concatenação de Arrays

arr3 = np.concatenate([arr1, arr2]) # temos que passar uma LISTA de arrays para concatenar
print(arr3)

# broadcasting
print(5 * arr3) # No python podemos fazer operação entre dados de diferentes tipos