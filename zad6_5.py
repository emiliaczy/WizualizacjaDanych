import numpy as np 
def odw(n):
    x = np.array([i for i in range(n,0,-1)])
    diag = np.diag([x for x in range(n,0,-1)])
    print(diag)
odw(5)