class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __lt__(self,drugi):
        return self.x < drugi.x

    def __le__(self, drugi):
        return self.x<=drugi.x
    
    def __gt__(self,drugi):
        return self.x>drugi.x

    def __ge__(self, drugi):
        return self.x>=drugi.x
        
kw = Kwadrat(10)
kw2 = Kwadrat(9)
print(kw<=kw2)
print(kw>kw2)
if kw>=kw2:
    print("Jest wiekszy lub rowny")
else:
    print("Nie jest wiekszy lub rowny")

if kw<kw2:
    print("Jest mniejszy")
else:
    print("Nie jest mniejszy")


