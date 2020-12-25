class car:
    guma=4                  #STATIC (class varijabla)
    def __init__(self):
        self.vrata=2
        self.marka="bmw"   #INSTANCE
        self.boja="crvena"
c1=car()
c2=car()
print(c1.vrata,c1.guma,c1.marka)
print(c2.vrata,c2.guma, c2.marka)
c1.vrata=4
print(c1.vrata,c1.guma,c1.marka)
print(c2.vrata,c2.guma,c2.marka)
car.guma=8 #ovo je statična varijabla i promeniće se svuda, ne samo kod jednog!
car.boja="žuta" ###NE MENJA, SAMO SE MOGU ZA SVE MENJATI STATIČNE VARIJABLE, IZVAN KONSTRUKTORA.
print(c1.vrata,c1.guma,c1.marka,c1.boja)
print(c2.vrata,c2.guma,c2.marka,c2.boja)