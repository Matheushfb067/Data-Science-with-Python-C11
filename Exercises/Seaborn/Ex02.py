'''
2. Utilizando do dataset titanic, proponha um gráfico que apresente a
distribuição das idades dos passageiros, diferenciando os dados por sexo e
incluindo uma curva de densidade (KDE);
'''

import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')
print(ds_titanic)

sns.histplot(
    data = ds_titanic,
    x = 'age',
    hue = 'sex', # Separando por categoria male e female
    kde = True
)
plt.show()