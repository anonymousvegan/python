#napraviti program u pyhtonu gde se pravi rečnik imena i prezimena
#prvih 5 učenika odeljenja, gde je ključ redni broj u esdnevniku,
#a vrednost ime i prezime učenika.
#potom odštampa ceo rečnik, pa odštampati ključeve, pa odštampati vrednosti

# Vahid Agusevic
# Amar Alijevic
# Ismet Aljovic
# Ajna Omerovic
# Hena Dolovac

ucenici = {1: "Vahid Agusevic", 2: "Amar Alijevic", 3: "Ismet Aljovic", 4: "Ajna Omerovic", 5: "Hena Dolovac"}

for kljuc, vrednost in ucenici.items():
    print (kljuc, ": ", vrednost)

for kljuc, vrednost in ucenici.items():
    print (kljuc)
    
for kljuc, vrednost in ucenici.items():
    print (vrednost)