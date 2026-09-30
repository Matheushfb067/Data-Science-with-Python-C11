import matplotlib.pyplot as plt
import numpy as np

# Plotando graficos com Plot
x = np.array([1, 2, 3, 4])
y = x * 2

# Novo eixo y
y2 = x * x

# label das coordenadas de x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Plots multiplos de forma conjunta
# Passamos uma sequencia de coordenadas x, y e string de customização no formato: 

# Plotando dois graficos no mesmo plano
plt.plot(x, y, 'r-', x, y2, 'b--')
plt.show()