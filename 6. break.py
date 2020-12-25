x=int(input("koliko kilograma banana kupuješ?"))
i=1
imam=10
while i<=x:
    if i>imam:
        print("nemamo toliko, daćemo sve što imamo")
        break
    print("1kg")
    i+=1
print("doviđenja")

#### pisanje svih brojeva, sem deljivih sa 3 
for i in range(1,101):
    if i%3==0:
        continue    #preskače i odmah ide na sledeći
    print(i)
print(i)
#ukratko, break izlazi iz celog loop-a, continuo preskače jedan loop
for z in range(10):
    if z==3:
        continue ###preskače 3
    if z==4: #bez pass izbacio bi error!
        pass ###preskače ovaj deo koda, koristim pas kad želim kasnije nastaviti taj deo koda!
    if z==6:
        break #ne ispisuje 6, već izlazi iz loopa.
    print(z)
def mojafunkcija():
    pass #kasnije ću upisati nešto u funkciju
print(1+2)