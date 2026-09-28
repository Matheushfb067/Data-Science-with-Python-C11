import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

''' Grafico de Histograma - representa a distribuição de dados numericos em intervalos (bins), 
o que permite visualizar como os valores se concentram ao longo de uma escala '''

# todo datasset do seaborn são datasets do pandas

ds_penguins = sns.load_dataset('penguins')
# print(ds_penguins)

# Setando um estilo diferente no grafico
sns.set_style('dark')

# Setando uma fonte maior
sns.set_context('notebook')

# Criando bins onde cada bin representa um tipo de pinguim
sns.histplot(
    data = ds_penguins, # Passando o dataset 
    x = 'flipper_length_mm', # Tamanho do bico do pinguim
    hue = 'species', # quebrando a latinha (bins) por especies - separando por raças
    kde = True, # traça linhas sobre os dados de cada um dos pinguins
)
plt.show()

