class telefon:
    def __init__(self,ram, inter):
        self.ram=ram
        self.inter=inter
    def update(self):
        self.inter=512
    def uporedi(self,drugi):
        if self.inter==drugi.inter:
             return True
        else:
            return False
mi10=telefon(8,256)
s20ultra=telefon(16,256)
def poređenje():
    if mi10.uporedi(s20ultra):
        print("imaju istu internu memoriju")
    else:
        print("nemaju istu memoriju")
poređenje()
### zamena interne memorije
s20ultra.update()
poređenje()