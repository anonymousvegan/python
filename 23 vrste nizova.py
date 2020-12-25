from numpy import array, linspace, arange, logspace, zeros, ones
a=array([1,2,3,4,5]) #običan niz
print(a)
print(a.dtype)
b=array([1,2,3,4,5],float) #konvertuje sve u float
print(b,b.dtype)
c= linspace(0,10,5) #prvi boj će biti 0, poslednji 10. biće ukupno 5 delova.
d=linspace(0,10,6) # 0, 2 , 4, 6, 8, 10 #float
print(c, d)
e=arange(1, 10, 2)
f=range(1,10,2)
print(e,f) #range se ne može ispisati kao niz. ostalo je isto.
for i in f:
    print(i,end="")
g=logspace(1, 10, 10, True, 2, float)   # dva na 1 do 2 na 10, 10 delova, baza 2(podrazumevano 10),
#tip float, uzima zadnju vrednost.
print()
print(g) ###ispisuje, sa e+01 formatom. 
i=0
while i<10:
    print("%.2f" %g[i])
    i+=1
h=logspace(1, 10, 10, True, 3, float)
i=0
while i<10:
    print("%.2f" %h[i])
    i+=1
#FOR LUP OVDE NE RADI!
o=ones(5)
z=zeros(7,int)
t=zeros(7,bool)
print(o,z,t)