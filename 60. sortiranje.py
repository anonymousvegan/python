def sortiraj(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
lista=[5,3,8,6,7,2]
sortiraj(lista)
print(lista)
lista2=[5,3,8,6,7,2]
lista2.sort()
print(lista2)