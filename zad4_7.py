class Robaczek:
    def __init__(self):
        self.x=0
        self.y=0
        self.krok=1
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow*self.krok
        return self.y 
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow*self.krok
        return self.y
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow*self.krok
        return self.x
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow*self.krok
        return self.x
    def pokaz_gdzie_jestes(self):
        return self.x, self.y


ster = Robaczek()
print(ster.idz_w_gore(2))
print(ster.idz_w_dol(4))
print(ster.idz_w_lewo(6))
print(ster.idz_w_prawo(6))
print(ster.pokaz_gdzie_jestes())


