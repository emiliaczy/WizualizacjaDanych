import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',sep=";")


x = df.groupby(["Sprzedawca"]).agg({"idZamowienia":['count']})
wykres = x.plot.bar()
wykres.legend()
wykres.set_ylabel('Ilość')
wykres.set_xlabel('Sprzedawca')
plt.title('Suma złożonych zamówień')
plt.show()