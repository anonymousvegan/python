#tip je none, otprilike kao null u ostalim jezicima
a=None
print(type(a))
#imamo 4 vrste brojeva:
prvi=1  #INT
drugi=3.14 #FLUAT
treci=1+5j #COMPLEX
cetvrti=True #BOOL
#pretvaranje 
print(prvi,drugi,treci,cetvrti)
uInt= int(drugi) #3
uFloat=float(prvi) #1.0
uComplex= complex(prvi,drugi)
ubool= bool(prvi)
izbool= int(cetvrti)
print(uInt,uFloat,uComplex, ubool, izbool)
##sequence#######################################################################
lista=[1,2,3,4,5] #list
skup={1,2,3,4,5} #set
t=(23,4,5,6) #tuple
print(type(lista))
print(type(skup))
print(type(t))
string="nikola"
print(type(str))
##range ##  i dalje sekvenca ##
a=range(10)
print(a) #neće ispisati ništa sem range(0,10)! mora se pretvoriti u listu
b=list(range(10))
print(b)
c=list(range(3,20)) ##podrazumevano razmak je jedan, prvi broj je nula, zadnji-1 se mora uneti.
d=list(range(3,20,4))
print(c,d)
##rečnik (mapa)#############################################################
osoba={"ime":"nikola","prezime":"matković"}
print(osoba["ime"])