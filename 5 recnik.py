osoba={"ime": "nikola", "prezime":"matkovic"}
print(osoba["ime"])
print(osoba.get("ime", "not found"))
print(osoba.get("godine", "not found"))
imena=["milica", "tamara", "anđela"]
prezimena=["ilic", "markovic", "komatina"]
osobe=dict(zip(imena, prezimena))
print(osobe)
osobe["milica"]="kolašinac"
del osobe["anđela"]
person = {"ime":"nikola", "prezime":"matković", "godine":"17", "životinje": ["krava","mačka","pas"], "škole": {"loše":"tenička", "dobre": ["gimnazija", "osnovna"] } }
print(person["ime"])
print(person["životinje"])
print(person["životinje"][1])
print(person["škole"]["dobre"])
print(person["škole"]["dobre"][1])
osoba1={"ime": "marko", "prezime":"marković"}
osoba2={"ime": "miroljub", "prezime":"petrovic"}
osoba1.clear()  #briše sve iz osoba 1
print(osoba1) #vraća {}, znači nema sadržaj ali i dalje postoji kao objekar
del osoba1 #ovo briše  za stalno, više ga ne možemo naći
osoba1={"ime": "marko", "prezime":"marković"}
osoba3=osoba1
osoba3["ime"]="miljan"
print(osoba3) # osoba 3 je zapravo samo veza ka osobi 1
print(osoba1) # rezultat će biti isti.
osoba1={"ime": "marko", "prezime":"marković"}
osoba4=osoba1.copy()
osoba4["ime"]="marijana"
print(osoba1,osoba4) #iskopirali su se bez referenci
nekiSkup={"a","e","i","o","u"}
vrednost="samoglasnik"
slova=dict.fromkeys(nekiSkup,vrednost)
print(slova)
print(slova.items()) #otprilike isto što i print
print(slova.keys()) #ispisuje samo ključeve
print(slova.values()) #ispisuje samo vrednosti
print(slova.pop("a","nije pronađen taj ključ")) #izbacuje ključ a
print(slova.pop("r","nije pronađen taj ključ")) #piše nije pronađen, jer je to defult, inače bi bio error 
slova.popitem() #slučajan izvacuje
print(slova)
slova=dict.fromkeys(nekiSkup,vrednost)
print(slova)
print(slova.setdefault("a","suglasnik")) #ako nađe a vraća vrednost a, ako ne vraća suglasnik, bez difult vraća none
print(slova.setdefault("r","suglasnik"))
slova.update()
brojevi={1:"jedan", 2:"dva",3:"četiri"} #namerna greška
ispravka={3:"tri"}
dodatak={4:"četiri"}
brojevi.update(ispravka)
brojevi.update(dodatak)
print(brojevi)