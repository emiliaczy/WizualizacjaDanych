import numpy as np 
def macierz(n):
    przek=[]
    for i in range(n):
        przek.append(2)            
    A = np.diag(przek) 
    for a in range(0,n):
        for b in range(0,n):
            for c in range(1,n+1):
                if(a==b+c or b==a+c):  
                    A[a,b]=2*(c+1)    
    return A                
        
print(macierz(3))