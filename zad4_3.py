with open ("plik.txt", "w") as plik:
    plik.write("Praca domowa\nWizualizacja Danych\nEmilia Czyrak")
    
with open("plik.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")