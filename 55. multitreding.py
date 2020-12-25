from threading import *
from time import sleep # metoda za spavanje
class androd(Thread):
    def run(self):                      #mora se zvati run!
        for i in range(500):
            print("samsung")
class ajfon(Thread):
    def run(self):                     #mora se zvati run!
        for i in range(500):
            print("ajfon")
tel1=androd()
tel2=ajfon()
tel1.start()                          #umesto run pišem start!
tel2.start()                          #umesto run pišem start!
#ispis neće biti ravnomeran, jer sistem ima zauzete tredove! 
# način da napravimo da raid je spavanje!
class windows(Thread):
    def run(self):                      #mora se zvati run!
        for i in range(10):
            print("windows")
            sleep(1)                    #1s
class linux(Thread):
    def run(self):                     #mora se zvati run!
        for i in range(10):
            sleep(1)                    #1s
            print("linux")
komp1=windows()
komp2=linux()
komp1.start()
sleep(0.2) #da ne bi bili ispisani u istoj liniji 
komp2.start()
komp1.join() # main čeka da završi t1
komp2.join() # main leka da završi t2
print("ćaoo") #biće is isano odmah, jer main tred ne radi ništa, već t1 i t2. zato mora join.