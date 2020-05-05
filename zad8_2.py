import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

## 2 a) #######

print(df[df['Liczba']>1000])
print("\n")


## 2 b) ########
print(df[df['Imie']=='EMILIA'])
print("\n")

## 2 c) #######
print(df.agg({'Liczba':['sum']}))
print("\n")

## 2 d) ######
x =(df[((df.Rok > 2000) & ( df.Rok< 2005))])
print(x.agg({'Liczba':['sum']}))
print("\n")
## 2 e )######
d = (df[((df.Plec=='K'))].agg({'Liczba':['sum']}))
print("Urodzonych dziewczynek jest:{}".format(d))
print("\n")
c = (df[((df.Plec=='M'))].agg({'Liczba':['sum']}))
print("Urodzonych chlopcow jest:{}".format(c))
print("\n")

## 2 f) #####
df2 = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(df2, start=1):
    print(f"{index} {group[0]}")
    print(f"{group[1].iloc[0]['Imie']}", end=' ')
    print(f"{group[1].iloc[0]['Liczba']}")

## 2 g) ######
dz = (df[((df.Plec=='K'))].sort_values(by="Liczba"))
chl = (df[((df.Plec=='M'))].sort_values(by="Liczba"))
print(dz.tail(1))
print(chl.tail(1))



