from numpy import *
a=array([1,2,3,4,5,6])
a+=5
print(a)
b=array([1,2,3,4,5,6])
b*=5
print(b)
c=a+b
print(c)
print(sum(a))
print(log(a))
print(sin(a))
print(sqrt(a))
print(min(a))
print(max(a))
d=concatenate([a,b]) #spaja ova 2
print(d) 
niz1=array([1,2,3,4,5])
niz2=niz1
print(niz1, niz2) #iste cifre
print(id(niz1), id(niz2)) #isti id 
niz3=niz1.view()
print(niz3, id(niz1), id(niz3))  # kopirani su oba, id je drugačiji, ali i dalje su vezani
niz1[2]=15
print(niz1) ###oba su promenila
print(niz3) ###svoju vrednost
niz4=niz1.copy() #potpuno kopiranje
print(niz4, id(niz4))