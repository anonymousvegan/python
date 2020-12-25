## ako imamo.
## class nešto:
## metoda(a,b,c):
## metoda(a,b): tako nešto  se naziva overloading metode- i to NE RADI u pythonu.
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):   ####dinamično menjanje u zavisnosti od broja argumenata- overloading
        s=0                               ###ovo  je trik kako da radi, u ostalim jezicima nije potrebno ovo.
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None and c==None:
            s=a+b
        elif a!=None and b==None and c==None:
            s=a
        return s
s1=student(12,23)
print(s1.sum(4,5,4))

class x:
    @staticmethod
    def prikaži():
        print("prikaz iz x")
class y(x):  ###################iako nasleđuje x, metoda biva overridovana  jer postoji i ovde.
    @staticmethod
    def prikaži():
        print("prikaz iz y")
b=y()
b.prikaži()