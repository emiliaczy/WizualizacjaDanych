import numpy as np 
import pandas as pd

df = pd.read_csv('zamowienia.csv',sep=";")
## 3 a) #######

print(df["Sprzedawca"].unique())
print("\n")

### 3 b) ######

print(df.sort_values(by="Utarg").tail(5))
print("\n")

## 3 c) #######
print(df.groupby(["Sprzedawca"]).agg({"idZamowienia":['count']}))
print("\n")

## 3 d) #######

print(df.groupby(["Kraj"]).agg({"idZamowienia":['count']}))
print("\n")
## 3 e) #####
suma=(df[((df.Kraj == "Polska") & (df.DataZamowienia>"2004-12-31") & (df.DataZamowienia<"2006-01-01"))].agg({"idZamowienia":['count']}))
print(suma)
print("\n")
## 3 f) #####
sredni=(df[((df.DataZamowienia>"2003-12-31") & (df.DataZamowienia<"2005-01-01"))].agg({"Utarg":['average']}))
print(sredni)
## 3 g) ####
plik = open("Zamowienia_2015.csv","w+")
plik.write(str(suma))
plik.close()
plik2 = open("Zamowienia_2014.csv","w+")
plik2.write(str(sredni))
plik2.close()
