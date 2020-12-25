a=10
b=13
def mojafunkcija():
    a=3
    print(a) #a je u ovo slučaju lokalno jer je deklarisano u funkciji. važi samo za tu funkciju.
    print(b) #b se može koristiti u funkciji jer je globalno, ali menjanje će kreirati novu lokalnu B!
mojafunkcija() #a=13 u f, b=13 u g
print(a)  #a-g-10.
##korišćenje globalne u funkciji
marka="xiaomi"
def funkcija():
    global marka
    marka="samsung"
    print(marka)
funkcija()
#korišćenje globalne i lokalne
mreza="vip"
def kartica():
    mreza="mts" #ne menja globalnu varijablu
    print("local",mreza)
    y=globals()["mreza"] #y=vip
    print("global y",y)
    #y="telenor"            POGREŠNO!
    globals()["mreza"]="telenor" #ISPRAVNO!
kartica()
print(mreza)