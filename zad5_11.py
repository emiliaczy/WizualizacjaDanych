def fib(n):
    a, b = 0, 1
    for a in range(n):
        a, b = b, a + b
        yield a

ciag=fib(10)
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))

print("\n\n")
#Drugi sposob na wywolanie:
ciag2=fib(5)
for i in ciag2:
    print(i)
