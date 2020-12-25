from array import *
niz=array("i",[]) # prazan niz
duzina=int(input("koliko vredosti želite da ubacite u niz"))
for i in range(duzina):
    unos= int(input("unesi sledeći broj"))
    niz.append(unos)
print(niz)
###korisnik traži neku vrednost:
trazi=int(input("koju vrednost tražite  u nizu"))
k=0
for e  in niz:
    if e==trazi:
        print(k)
        break
    k+=1
### lakši način:
trazi=trazi=int(input("koju vrednost tražite  u nizu"))
print(niz.index(trazi))