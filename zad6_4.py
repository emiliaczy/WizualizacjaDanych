import numpy as np 

def generuj(x,n):
    return np.logspace(1,n,n,base = x)

print(generuj(3,4))