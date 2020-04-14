class Samogloska:
    
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if(isinstance(self.data, str)):
            if self.index>=len(self.data):
                raise StopIteration
            if self.data[self.index] in ("a","e","i","o","u","y"):
                print(self.data[self.index])
            self.index+=1
        else:
            print("To nie string.")


s=Samogloska("uniwerystet")
for i in s:
    i

print("\n\n")

s2=Samogloska("olsztyn")

for i in s2:
    i
