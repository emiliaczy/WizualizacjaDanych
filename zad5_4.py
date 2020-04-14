class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(8,2)
p2 = Point(9,7)
print(p1.counter)
p2.update(4)
print(p2.counter)
print(p1.counter)
for i in range(5):
    p1.update(i)
print(p1.counter)
print(p2.counter)