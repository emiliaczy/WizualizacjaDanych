class NaZakupy:
    def __init__(self,nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def __del__(self):
        print("bye")
    
    def wyswietl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed
    
    def ile_kosztuje(self):
        return str(self.ilosc * self.cena_jed) + "zł."
    def ile_produktu(self):
        return str(self.ilosc)+ self.jednostka_miary


zakupy = NaZakupy("maslo", 5, "szt.",6)
print(zakupy.wyswietl_produkt())
print(zakupy.ile_kosztuje())
print(zakupy.ile_produktu())
