import matplotlib.pyplot as plt
import numpy as np

# Plotando graficos com Plot
x = np.array([1, 2, 3, 4])
y = x * 2

# label das coordenadas de x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Existe um novo argumento que pode ser passado para um plot para mudar seu formato
# É uma string que pode ser montada usando o padrão: fmt = [marker][line][color]

# Formatando o estilo dos plots
plt.plot(x, y, 'o:g', linewidth=3, markersize=20)
plt.show()