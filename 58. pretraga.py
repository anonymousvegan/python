pozicija=-1
def pretraga(lista, n):
    i=0
    while i<len(lista):
        if lista[i]==n:
            globals()["pozicija"]=i
            return True
        i+=1
    return False
lista=[12,23,5,23,541,65,2]
n=23
if pretraga(lista,n):
    print("nađeno",pozicija)
else:
    print("nije nađeno")