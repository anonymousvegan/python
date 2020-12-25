def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)
#adresa će biti ista 
#u početku, ali kasnije ne
#vrednost od a se neće promeniti.

#liste će se menjati za razliku od varijabli
def izmeni(l):
    print(id(l))
    lista[1]=25 #izmena je moguća!
    print("lista",l)
lista=[1,2,3]
print(id(lista))
izmeni(lista)
print("lista2",lista) 