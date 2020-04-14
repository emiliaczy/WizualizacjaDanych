class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        return self.rodzaj

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
        Material.__init__(self,rodzaj,dlugosc,szerokosc)
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        return self.rozmiar, self.kolor, self.dla_kogo,self.rodzaj,self.dlugosc,self.szerokosc
        

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra,rozmiar,kolor,dla_kogo,dlugosc,szerokosc):
        Ubrania.__init__(self, rozmiar,kolor,dla_kogo,"Sweter",dlugosc,szerokosc)
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        return self.rodzaj_swetra

ub = Ubrania("L","czarny","damski","koszula","60","50")
print(ub.wyswietl_dane())
print(ub.wyswietl_nazwe())
sw = Sweter("z kapturem","M","szary","męski","65","55")
print(sw.wyswietl_dane())
print(sw.wyswietl_nazwe())