# Conceito mais importante do numpy: 
# Condicionais no NumPy

import numpy as np

# Plantando seed aleatoria
np.random.seed(10)

# Estruturando matriz 3 por 3 
mtz = np.random.randint(1, 99, 9).reshape(3, 3)
print(mtz)

print("")

# Mostre apenas os elementos menores que 70: 

# print(mtz < 70) # <- broadcasting - indica quais elementos são true = menor que 70 e false = maiores que 70
print(mtz[mtz < 70]) # Mostra os elementos da matriz menores que 70 com os numeros de fato ao em vez de True e False

# Retornando apenas os numeros pares dessa matriz
# print(mtz % 2 == 0) <- Mostrando com True e False
print(mtz[mtz % 2 == 0]) # <- pegando já sem a mascara de true e false
