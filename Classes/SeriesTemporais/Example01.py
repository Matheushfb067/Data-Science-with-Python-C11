import matplotlib.pyplot as plt
import pandas as pd

dataset  = pd.read_csv('retail_index_br.csv', delimiter=';', index_col = 'date', parse_dates = True)
print(dataset)

# Transformando dados de y em float
dataset['retail_index'].astype(float)

# Plotando a time series
dataset['retail_index'].plot(
    figsize=(8, 6),
    title='Índice de volume de vendas no setor varejista brasileiro',
    xlabel='Data', 
    ylabel='Índice', 
    x_compat=True
)
plt.show()