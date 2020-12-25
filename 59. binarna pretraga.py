# ovo ubrzava pretragu pod uslovom da je lista sortirana
pozicija=-1
def pretraga(sortiranalista, n):
    l=0
    u=len(sortiranalista)-1
    while l<=u:
        m=(l+u)//2
        if sortiranalista[m]==n:
            globals()["pozicija"]=m
            return True
        else:
            if sortiranalista[m]<n:
                l=m+1
            else:
                u=m-1
    
sortiranalista=[12,23,54,231,541,655,2999]
n=23
if pretraga(sortiranalista,n):
    print("nađeno",pozicija)
else:
    print("nije nađeno")