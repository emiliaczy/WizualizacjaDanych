class Wspak:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


for i in Wspak("kwarantanna"):
    print(i)

print("\n")

for i in Wspak("uniwersytet"):
    print(i)

print ("\n")
#Drugi sposob na wywolanie:
x = Wspak("dom")
print(x.__next__())
print(x.__next__())
print(x.__next__())


