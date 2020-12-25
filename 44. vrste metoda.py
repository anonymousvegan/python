class ucenik:
    drzava="srbija"
    def __init__(self,ime,skola,srpski,matematika,biologija): #konstruktor,instance
        self.ime=ime
        self.skola=skola
        self.srpski=srpski
        self.matematika=matematika
        self.biologija=biologija
    def prosek(self):
        return (self.srpski+self.matematika+self.biologija)/3 #instance metoda
    def get_ime(self):                                        #instance getter metoda () accesor
        print(self.ime)
    def set_skola(self):                                      #instance setter metoda () mutator
        self.skola="osaonica"
    @classmethod
    def prebivalište(cls):                                    #class metoda - argument ne  mora biti cls, valjda.
        print(cls.drzava)                                     #cls se odnosi na klasu!
    @staticmethod
    def nebitnametoda():                                      #statična metoda
        print("danas je divan dan")                           #metoda radi nešto nebito, nevezano za klasu i varijable.
ucenik1=ucenik("nikola","gimnazija",4,4,5)
print(ucenik1.prosek())
ucenik1.get_ime()
ucenik1.set_skola()
print(ucenik1.skola)
ucenik1.prebivalište()
ucenik1.nebitnametoda()
