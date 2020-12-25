a=10
b=a
print(a,b)
print(id(a))
print(id(b))
print(id(10))  #sve 3 vraćaju isto!
c=10
print(id(c)) #isto će biti
a=9
print("a=",id(a))
print(id(b))
print(id(c))
c=8
print("a=",id(a)) #menjaju se svi
print("b=",id(b))
print("c=",id(c))
PI=3.14
print(type(PI)) # vraća tip
