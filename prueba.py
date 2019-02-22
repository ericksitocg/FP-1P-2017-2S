import numpy as np

a = np.array(["a","b","c","d"])
numeros = np.array([12,32,321,433,54,120])

#indexacion booleana
indices = numeros > 300
print( numeros[indices] < 400)

