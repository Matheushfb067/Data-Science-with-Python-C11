import matplotlib.pyplot as plt
import numpy as np

# Plotando graficos com Plot
# Cada função do pyplot muda uma caracteristica do grafico

x = np.array([1, 2, 3, 4])
y = x * 2

# label das coordenadas de x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.plot(x, y)
plt.show()