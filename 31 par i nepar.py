
def funckija(lst):
    parnih=0
    neparnih=0
    for i in lst:
        if i%2==0:
            parnih+=1
        else:
            neparnih+=1
    return parnih, neparnih
lst=[1,2,3,4,5]
par, nepar = funckija(lst)
print(par,nepar)
print("parnih ima {}, a neparnih {}".format(par,nepar)) ###string.format!
