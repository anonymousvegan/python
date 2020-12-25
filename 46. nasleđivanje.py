class A:
    def mogucnost1(self):
        print("mogućnost 1 radi")
    def mogucnost2(self):
        print("mogućnost 2 radi")
class B(A):                        #b će imati sve mogućnosti a klase
    def mogucnost3(self): 
        print("mogućnost 3 radi")
    def mogucnost4(self):
        print("mogućnost 4 radi")
class C:                        #b će imati sve mogućnosti a klase
    def mogucnost5(self):
        print("mogućnost 5 radi") #c ne nasleđuje ni jednu klasu, IMA SAMO MOGUĆNOST 5
class D(C,B):                     #D NASLEĐUJE SVE KLASE, NE MOŽE NASLEDITI I A I B UJEDNO!
    def mogucnost6(self):
        print("mogućnost 6 radi")

b1=B()
b1.mogucnost1()
b1.mogucnost2()
b1.mogucnost3()
b1.mogucnost4()
c1=C()
c1.mogucnost5()
d1=D()
d1=D()
d1.mogucnost1()
d1.mogucnost2()
d1.mogucnost3()
d1.mogucnost4()
d1.mogucnost5()
d1.mogucnost6()