# Importando Datasets no NumPy

import numpy as np

# Criando uma variavel para receber o datasset
dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str') # Delimiter informa o python o delimitador usado no csv
print(dataset)

print("")

# NO TERMINAL MOSTRA SOMENTE O INICIO E O FIM DO QUE ESTAMOS FILTRANDO ARQUIVO CSV POR CONTA DE SEU TAMANHO, COMO NOS EXEMPLOS ABAIXO

# Extraindo as colunas do dataset
print(dataset[0, :])

# Extraindo o nome das empresas
print(dataset[:, 1])
# Cortando o nome da coluna para printar o nome das empreas
print(dataset[1:, 1])
# Extraindo o nome das empresas porem sem mostrar repetidamente
print(np.unique(dataset[1:, 1]))
# # Extraindo o nome das empresas porem sem mostrar repetidamente contando quantas missões cada empresa teve
print(np.unique(dataset[1:, 1], return_counts='True'))