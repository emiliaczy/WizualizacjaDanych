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
        
    def __add__(self,bok):
        wynik = self.x+bok.x
        return "Nowy bok kwadratu:{}".format(wynik)

    
    

kw = Kwadrat(5)
kw2=Kwadrat(10)
kw3= kw+kw2
print(kw3)
