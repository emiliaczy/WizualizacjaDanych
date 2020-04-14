class Parzysty:
    def __init__(self, data):
        self.data=data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        if self.index % 2 ==0:
            print(self.data[self.index])
        self.index+=1
        

for i in Parzysty("Uniwersytet"):
    i

print("\n\n")

for i in Parzysty("Kwarantanna"):
    i






