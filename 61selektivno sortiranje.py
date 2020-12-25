def sortiraj(lista):
    for i in range(len(lista)-1):
        pozicijanajmanjeg=i
        for j in range(i,len(lista)):
            if lista[j]<lista[pozicijanajmanjeg]:
                pozicijanajmanjeg=j
        lista[i],lista[pozicijanajmanjeg]=lista[pozicijanajmanjeg],lista[i]
lista=[5,3,8,6,7,2]
sortiraj(lista)
print(lista)
