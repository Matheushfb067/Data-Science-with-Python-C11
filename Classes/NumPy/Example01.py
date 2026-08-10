import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
print(type(arr))

# Propriedades do array

mtz = np.array([[10, 20],[30, 40],[50, 60]])
print(mtz) 
print(arr.size) # tamanho do array
print(arr.ndim) # dimensões do array
print(arr.shape) # Formato do array 

mtz = np.ones((5, 5))
print(mtz)

# Zeros
arr = np.zeros(10) # 
print(arr.reshape(5, 2)) # Transforma o array unidimensionais em bidimensionais

# Arrange - define a sequencia de elementos que irá aparecer na matriz

mtz = np.arange(2, 21, 2) # criou uma lista de 2 a 20 de dois em dois
print(mtz)
