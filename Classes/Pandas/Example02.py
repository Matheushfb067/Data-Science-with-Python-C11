import pandas as pd
import numpy as np

s1 = pd.Series({'v1': 10, 'v2': 45, 'v3': 70})
s2 = pd.Series({'v1': 10, 'v4': 50, 'v3': 70})

print(s1)
print(s2)

print("")

# Operações com Series
    # Aqui ao em vez de fazer as operações indice a indece, ele opera label a label

print(s1 + s2)
print("")
# Soma usando o metodo add() a vantagem disso é que podemos passar parametros para o metodo, como o exemplo abaixo
print(s1.add(s2, fill_value = 0)) 