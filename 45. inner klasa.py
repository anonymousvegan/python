class covek:
    def __init__(self,ime,godine):
        self.ime=ime
        self.godine=godine
        self.lap=self.laptop()
    def prikazi(self):
        print(self.ime,self.godine)
    class laptop:
        def __init__(self):
            self.brend="dell"
            self.ram=4
        def prikazi(self):
             print(self.brend,self.ram)
čovek1=covek("nikola",17)
čovek2=covek("mihajlo",24)
čovek1.prikazi()
lap1=čovek1.lap
lap1.prikazi()