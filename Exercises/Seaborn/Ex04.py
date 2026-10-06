'''
4. Utilizando do dataset mpg, analise a relação entre a potência dos
veículos (horsepower) e o consumo de combustível (mpg), construindo uma
visualização que permita identificar a tendência entre essas variáveis e
interpretar seu comportamento;
'''

import matplotlib.pyplot as plt
import seaborn as sns

ds_mpg = sns.load_dataset('mpg')
print(ds_mpg)

sns.regplot(
    data = ds_mpg,
    x = 'horsepower',
    y = 'mpg',
    line_kws = {'color': 'red'}
)
plt.show()