import matplotlib.pyplot as plt
import numpy as np

# Plotando graficos com Plot
x = np.array([1, 2, 3, 4])
y = x * 2

# Novo eixo y
y2 = x * x

''' As vezes queremos multiplos graficos de uma vez, porem de forma separada no 
matplotlib isso por ser feito por meio da função subplot '''

plt.subplot(1, 2, 1) # Uma linha, duas colunas, posição 1
plt.title('Linear') # Titulo do Grafico
plt.plot(x, y, 'r-') # 'r-' r de red e - de continua -> linha vermelha continua

plt.subplot(1, 2, 2) # Uma linha, duas colunas, posição 2
plt.title('Exponencial') # Titulo do grafico
plt.plot(x, y2, 'b--') # Linha azul tracejada

plt.show()