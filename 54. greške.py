a=5
b=0
####običan traj
try:
    print(a/b)
except Exception:
    print("nemoguće je deliti nulom")
print("ćaooo")
#traj koji ispisuje grešku- e je greška.
m=5
n=0
try:
    print(a/b)
except Exception as e: 
    print("nemoguće je deliti nulom")
    print(e)
print("ćaooo2")
#komplikovanije:
x=5

try:
    print("fajl otvoren")  #zamisli da je fajl otvoren
    y=int(input())
    print(x/y)
except ValueError as e:
    print("pogrešan broj! kod greške: {}".format(e))
except ZeroDivisionError as e: #ZA SLUČAJ DA KORISNIK UNESE 0:
    print("nemoguće je deliti nulom! kod greške: {}".format(e))
except Exception as e:
    print("nepoznata greška! kod grešek: {}".format(e))
finally:
    print("fajl je zatvoren") #######finaly se izvršava u oba slučaja, i sa i bez greške.