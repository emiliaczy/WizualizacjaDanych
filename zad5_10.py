import itertools 
zbior = [1,2,3,4,5,6,7,8,9,10]
zbior2=[2,3,4,5,6,7,8,9,10,11]
x = itertools.combinations(zbior, 3)
y = itertools.combinations(zbior2, 3)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("\n\n")
#Drugi sposob na wywolanie:
for i in y:
    print(i)







    
