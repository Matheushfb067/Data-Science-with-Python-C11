import pandas as pd
import numpy as np

# É necessario passar uma lista de labels e uma lista de valores

# FORMA PADRÃO DE PREENCHER UMA SERIES
labels = ['Tiago', 'Matheus', 'Bruna', 'Julia']
valores = [23, 25, 27, 22]

# Criando a Series
se1 = pd.Series(index = labels, data = valores)
print(se1)
print(type(se1))

print("")

# Acessando elementos de uma Series
print(se1['Matheus']) # Mostra apenas o valor e não a chave
print(se1[['Matheus', 'Julia']]) # Como quero saber a informação de mais de uma pessoa, mostra a chave e o valor

print("")