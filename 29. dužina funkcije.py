def osoba(ime, **ostalo):  # **smeštaju sve podatke u ostalo, prave rečnik.
    print(ime)
    for i, j in ostalo.items():
        print(i,j)
    print(type(ostalo)) #dictonary-rečnik.
osoba("nikola", godine=17, zanimanje="programer",jezik="python")