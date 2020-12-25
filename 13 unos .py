x=int(input("unesi vrednost "))
y=int(input("unesi"))
print(x+y)
string=input("kako se zoves")
ch=input("unesi prvo slovo imena")[0] ## zapravo, moze uneti koliko hoce ali samo 1  ce se vaziti.
print(string,ch)
rezultat= eval(input("unesi matematicki zadatak")) #racuna sam, isto kao u js-u
print(rezultat)  #nije potrebna konverzija stringa u int.
from sys import argv ### argv radi u konzoli kad upises python ime var var - stim sto index 0 nosi ime.
a= int(argv[1])
b= int(argv[2])
print(a,b, argv[0]) #probaj u konzoli!