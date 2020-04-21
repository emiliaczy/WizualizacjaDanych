import numpy as np 
def fib(n):
    wyn = [1,1]
    for i in range(n-2):
        wyn.append(wyn[i] + wyn[(i + 1)])
    a = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    i = 0
    k = 0
    l = 0
    while i < n:
        if l==5:
            k+=1
            l=0
        a[k][l] = wyn[i]
        i+=1
        l+=1
        
    return a
print(fib(25))