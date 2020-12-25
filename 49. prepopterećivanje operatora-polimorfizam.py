a=1
b=2
print(a+b)
print(int.__add__(a,b)) #isto
print(int.__sub__(a,b)) 
print(int.__mul__(a,b)) 
print(int.__truediv__(a,b))
class brojevi:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ostali): 
        x=self.x+ostali.x
        y=self.y+ostali.y
        return brojevi(x,y)
    def __gt__(self,ostali):
        najveci=max(self.x,self.y,ostali.x,ostali.y)
        if najveci==self.x:
            return True
        elif najveci==self.y:
            return True
        else:
             return False
    def __str__(self):                                #kom3 radi!
        return "{} {}".format(self.x,self.y)  
prvi=brojevi(30,41)
drugi=brojevi(12,43)
#OVO NEĆE RADITI dok se ne definiše add funkcija.  
treci=prvi+drugi
print(treci.x,treci.y)
# ako je veći broj u prvom veći od većeg broja u drugom ispiši "tjt", u suprtnom"jok".
if prvi>drugi:
    print("tjt")
else:
    print("jok")
## želim da ispiše vrednosti a ne adresu! kom3
print(prvi)