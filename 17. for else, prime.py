lista=[1,2,3,4,5,6,7,8,9]
for i in lista:
    if i%5==0:
        print(i)
        break
else:                               #ovo je for else, kad bi bio tab desno- 5x bi se ispisalo!
    print("nema deljivog sa 5")     ## i ovo 
####################prime
num=11
for i in range(2, num//2): 
    if num % i == 0: 
        print("nije prost") 
        break
else: 
    print("prost")