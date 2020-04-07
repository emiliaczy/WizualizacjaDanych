class slowa ():
    def __init__ (self, slowo1, slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def czy_palindrom(self):
        if self.slowo1 == self.slowo1[::-1]:
            return "Słowo {} jest palindromem.".format(self.slowo1)
        return "Słowo {} nie jest palindromem.".format(self.slowo1)
    def czy_metagramy(self):
        roznica=0
        for i in range(len(self.slowo1)):
            for j in range (len(self.slowo2)):
                if self.slowo1[i]!=self.slowo2[j]:
                    roznica+=1
                i+=1
            if i>=len(self.slowo2):
                break
        if roznica==1:
            return "Słowa są metagramami." 
        return "Słowa nie są metagramami."
    
    def czy_anagramy(self): 

        if(sorted(self.slowo1)== sorted(self.slowo2)): 
            return "Słowa są anagramami."  
        else: 
            return "Słowa nie są anagamami."          
    
        

s=slowa("kajak","kapak")
print(s.czy_palindrom())
print(s.czy_metagramy())
s2=slowa("mata","tama")
print(s2.czy_anagramy())