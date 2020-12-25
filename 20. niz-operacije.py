from array import *
from math import pow
niz=array("i", [1,2,3,4,5])
print(niz)
for i in niz:
    print(i, end="")
print()
noviniz= array(niz.typecode, (a  for a in niz))
for y in noviniz:
    print(y)
niznakvadrat= array(niz.typecode, (int(pow(a,2)) for a in niz) ) #moglo je bez pow, samo a*a ali moram da komplikujem
# int mora ispred jer pow vraća float.
for x in niznakvadrat:
    print(x)
#pomoću while-a
z=0
while z<len(niznakvadrat):
    print(niznakvadrat[z])
    z+=1