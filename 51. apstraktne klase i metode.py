from abc import ABC, abstractmethod
class komp (ABC):                   #obavezno!
    @abstractmethod                 #obavezno!
    def program(self):
            pass                ## metoda bez tela je apstraktna, samim tim i klasa u kojoj je metoda.
class laptop(komp):
    def program(self):
        print("program radi")
# k1=komp()
# k1.program()                # radi ako ne importujem abc-ne ispisuje ništa,
lap1=laptop()
lap1.program()