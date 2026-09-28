import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

''' Diferença entre relação e correlação - A correlação mede o numero de relações porem de forma 
quantificada - numeros para medir as relações '''

''' Grafico de Heatmap - indica a correlação entre as variaveis que queremos descobrir se tem alguma 
relação entre si porem de maneira quantificada '''

ds_tips = sns.load_dataset('tips')
# print(ds_tips)

# Setando um estilo diferente no grafico
sns.set_style('dark')

# Setando uma fonte maior
sns.set_context('notebook')

# Selecionando as colunas que quero intentificar uma correlação
corr = ds_tips[['total_bill', 'tip', 'size']].corr()

# Quando um valor varia, o outro também tende a variar
sns.heatmap(
    data = corr,
    annot = True, # mostra os valores numéricos dentro de cada celula do heatmap
    fmt = '.2f' # duas casas decimais
)
plt.show()