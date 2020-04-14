months = ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
def miesiace():
    for m in months:
        yield m
         

mies = miesiace()
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))

print ("\n\n")
# Drugi sposob na wywolanie:
mies2 = miesiace()
for i in mies2:
    print(i)



