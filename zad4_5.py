class CiagiAryt():
    def pobierz_elementy(self):
        self.x1=input()
        self.x2=input()
        self.x3=input()
    def wyswietl_dane(self):
        return self.x1,self.x2,self.x3

    def pobierz_parametry(self):
        self.a1=input()
        self.a1=int(self.a1)
        self.r=input()
        self.r=int(self.r)
        self.n=input()
        self.n=int(self.n)
    
    def policz_sume(self):
        suma = (((2*self.a1+(self.n-1)*self.r)/2)*self.n)
        return("Suma elementow ciagu = {}".format(suma))

    def policz_elementy(self):
        suma=0
        if self.a1==self.n:
            return("Ilość elementów ciągu wynosi:{}".format(1))
        for i in range(self.a1,(self.n*self.r)+1,self.r):
            suma+=1
        return("Ilość elementów ciągu wynosi:{}".format(suma))
    
ciag = CiagiAryt()
ciag.pobierz_elementy()
print(ciag.wyswietl_dane())
ciag.pobierz_parametry()
print(ciag.policz_sume())
print(ciag.policz_elementy())



    
    
