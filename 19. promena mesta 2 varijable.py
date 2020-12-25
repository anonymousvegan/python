a=2
b=3
###zamena mesta bez temp varijable 
print(a,b)
a= a+b   #a= 2+3    a=5, b=3
print(a,b)
b=a-b    #b=5-3     a=5  b=2
print(a,b)
a=a-b    #a=5-2     a=3  b=2
print(a,b)
##### xor operator #### pojma nemam kako radi, ali je bolje rešenje
a= a ^ b
print(a,b)
b= a ^ b
print(a,b)
a= a ^ b
print(a,b)
#####  najlakši način
a,b=b,a
print(a,b)