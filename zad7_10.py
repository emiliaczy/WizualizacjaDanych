import numpy as np

a = np.arange(81).reshape(9,9)
print(a)

b = a.reshape(3,27)
print(b)

c = a.reshape(27,3)
print(c)

d=a.reshape(81,1)
print(d)

#to jedyne możliwosci, ponieważ liczba 81 nie ma więcej dzielnikow 
# i nie mozemy stworzyc innych wymiarow macierzy.


