class telefon:
    def __init__(self,rammemorija,internamemorija):    #ovo je konstruktor!
        self.ram =rammemorija
        self.inter=internamemorija
        print("konstrukcija završena")
    def config(self):
        print("ovaj telefon ima {}gb rama i {}gb interne memorije".format(self.ram,self.inter))

samsung_galaxy_s20_ultra=telefon(16,512)
samsung_galaxy_s20_ultra.config()
###konstruktor dobija vrednosti rama i interne.
#klasa dobija ram i inter varijablu
#ispisuje se da je konstrukcija završena
#kasnije se poziva metoda konfigurisanja- koja ovo ispisuje.