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

wspak = Wspak("emilia")
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())

print("\n")

wspak2=Wspak("dom")
print(wspak2.__next__())
print(wspak2.__next__())
print(wspak2.__next__())
print("\n")

for i in Wspak("kwarantanna"):
    print(i)



