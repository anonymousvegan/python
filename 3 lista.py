brojevi=[10,20,30,40,50,60]
print(brojevi[0])  #1s
print(brojevi[0:3]) #123
print(brojevi)
imena= ["nikola", "amer", "aldin"]
print(imena)
zajedno=[imena, brojevi]
print(brojevi[-3:-1])
brojevi.append(70) #dodaje 70 na kraj liste
print(brojevi)
brojevi.clear() #briše sve članove liste
print(brojevi)
brojevi=[1,2,3,4,5]
prvalista=["a","b","c"]
drugalista=prvalista
drugalista.append("d")  #ovo će promeniti obe liste, i prvi i drugu, jer su povezane.
print("prva:",prvalista) #koristimo zarez umesto +
print("druga:",drugalista) 
prvalista.clear()
drugalista.clear()
drugalista.append("e")
print("prva:",prvalista) # i dalje  povezane, sunisam našao način da ih otkačim.
print("druga:",drugalista)
treca=[11,12,13,14]
cetvrta=treca.copy()
cetvrta.append(15)
print("treca:",treca)
print("cetvrta:",cetvrta) #radi pravilno, tjt
samoglasnici=["a","e","i","o","i","u","r","i"]
brojslovaI=samoglasnici.count("i")
print(brojslovaI)
ribe=["saran","smuđ","pastrmka","ajkula"]
zivotinje=["detljić","kanarinac","vrabac"]
zivotinje.extend(ribe) #ovo će dodati sve ribe u listu životinja
print(zivotinje)
print(zivotinje.index("ajkula"))#vraća indeks ajkule
zivotinje.insert(0,"žaba") # radi isto što apend, samo ovde definišeš index.
print(zivotinje) #prvi se ne briše, samo se svi pomeraju desno.
zivotinje.pop(4) #briše 5.
print(zivotinje.pop(2)) ### ako se prita- ispisaće se na ekran i izbrisati, slično kao u js.
print(zivotinje)
zivotinje.remove("smuđ") # ovo je nešto kao pop samo se radi o elementu ne indeksu
print(zivotinje)
zivotinje.reverse() #unazad
print(zivotinje)
zivotinje.sort() #a-z
print(zivotinje)
zivotinje.sort(reverse=True) # z-a
print(zivotinje)
os=["windows", "linux", "andorid"]
osunazad=os[::-1] #pojma nemam kako ali ovo ispisuje unazad, naučiću vremenom :)
print(osunazad)
os.pop()#ovo briše zadnji element, znači zadnji ako ne unesem indeks.
print(os) 
os.append("ios")
os.append("solaris")
os[2]="simbian" #ovo će promeniti IOS u simbian.
print(os)
del os[2:]
print(os)
os.extend(["ubuntu","mint"]) # ovako se dodaje više stvari, obaveno je []
print(os)
numbers=[4,5,182,438,12,5]
print(min(numbers))
print(max(numbers))
numbers.sort()
print(numbers)