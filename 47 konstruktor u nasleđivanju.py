class A:
    def __init__(self):
        print("konstruktor iz A")
    def mogucnost1(self):
        print("mogućnost 1 radi")
class B(A):                      
    def mogucnost3(self): 
        print("mogućnost 3 radi")
b1=B() ### POZIVA KONSTURKTOR IZ A
class C:
    def __init__(self):
        print("konstruktor iz C")
    def mogucnost1(self):
        print("mogućnost 5 radi")
class D(C):                        
    def __init__(self):
        print("konstruktor iz D")
    def mogucnost3(self): 
        print("mogućnost 7 radi")
d1=D() ##poziva konstruktor iz D
### ako želimo oba:
class E:
    def __init__(self):
        print("konstruktor iz E")
    def mogucnost1(self):
        print("mogućnost 9 radi")
class F(E):                        
    def __init__(self):
        super().__init__()                  ####OBA RADE! NE ZABORAVI 2X ZAGRADE!
        print("konstruktor iz F")
    def mogucnost3(self): 
        print("mogućnost 11 radi")
F1=F()