from functools import reduce
f= lambda a,b: a+b  #iziii
print(f(5,3))
s= lambda a: a*a
print(s(21))
#### filter
def provera(n):
    return n%2==0   #1 or 0!
l=[15,62,356,8,23,1,68,9,2]
parni=(list(filter(provera,l)))  ## filter(funkcija, lista)
print(parni)
###lakši način:
neparni=list(filter(lambda n: n%2!=0, l))
print(neparni)
dupli=list(map(lambda n: n*2,parni)) #  primenjuje funkciju na sve članove liste
print(parni,dupli)
svi=reduce(lambda a,b: a+b, parni) # sabira i smešta u a, b biva sledeći broj, tako do kraja
print(svi)