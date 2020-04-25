import numpy as np 

a = np.array([[5,4,7],[9,0,2],[6,7,2]])
b = np.array([[3,5,6,7],[1,2,3,8],[4,4,8,3],[1,9,6,2]])
print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))