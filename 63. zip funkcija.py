a= ["nikola", "emin","amer"]
b= ["gimnazija", "tehnička", "osnovna "]
c=zip(a,b)
print(c)
l=list(c)
d=dict(zip(a,b))
s=set(zip(a,b))
print(l)
print(s)
print(d)
for (x,y) in c:
    print(x,y)