# Slicing no numpy

import numpy as np

# Plantando seed aleatoria
np.random.seed(10)

# Estruturando matriz 3 por 3 
mtz = np.random.randint(1, 99, 9).reshape(3, 3)
print(mtz)

# Iniciando Slicing na matriz
print("")
# Extraindo apenas a seunda linha da matriz 
print(mtz[1])

# Extraindo apenas a terceira coluna da matriz
print(mtz[:, 2])

print("")

# Extraindo a matriz 2x2 no canto inferior direito da matriz original
print(mtz[1:, 1:]) # pegando da primeira linha em diante e da primeira coluna em diante

print("")