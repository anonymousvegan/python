from array import *
import math
niz= array("i",[1,2,3,4,5,2])  ### niz se koristi najčešće za brojeve, i-integer, f/d-float, u-slova-izbegavati
#u nije podržan od verzije 3.3, valjda. koliko sam shvatio bolje koristiti numpy, array dobro funkcioniše sa c.
# niz je efikasniji u upotrebi memorije, i ima više funkcija.
print(niz) # ispisuje niz
print(niz.append(6))
print(niz)
print(niz.buffer_info()) #veličia niza i adresa u memoriji
lista=[10,11,12]
#    print(niz.byteswap()) nemam pojma čemu služi ####################################################
#    niz.clear() #briše sve iz niza, ne radi ##########################################################
print(niz.count(2))  ### koliko se puta neki broj/karakter pojavljuje u nizu
niz.extend(lista) #### odaje listu na kraj niza
niz.extend([13,14,15]) #može i ovako.
print(niz)
#niz.frombytes() #ne znam ##############################################################################
#niz.fromfile() ########################################################################################
#niz.fromlist() ########################################################################################
#niz.fromstring() ######################################################################################
print(niz.index(6))
niz.insert(5, 20) #na 6 će biti 20, niz se pomera u desno.
print(niz.itemsize) #ovde ne idu zagrade.
print(niz.typecode) #ni ovde, zato ih i pišem zajedno
print(niz.pop(4)) #uklanja i vraća-već viđeno.
print(niz.pop())
niz.pop()
print(niz)
niz.pop(6)
print(niz)
niz.remove(20) #uklanja  iz niza
print(niz)
niz.reverse() #obrće
print(niz)
#metode koje ne znam su tobytes, tofile, tolist, tostring.#######################################
print(max(niz))
print(min(niz))
print(niz[1])
niz[1]=100
print(niz)