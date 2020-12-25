def osoba(ime, godine=17): #defult vrednost godina je 17
    print(ime)
    print(godine)
osoba("nikola",17)
osoba(godine=54,ime="aleksa") 
osoba("nekonebitan") #17
def sabiranje(a, *b):
    print(a)
    print(b)
    print(type(b)) #tuple
    c=a
    for i in b:
        c+=i
    print(c)
sabiranje(1,2,3,4,5)
#bolji način:
def sum(*a):  # *znači sve ide u tuple.
    c=0
    for i in a:
        c+=i
    print(c)
sum(2,5)