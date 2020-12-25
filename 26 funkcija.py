def nikola():
    pass
def ispis():
    print("nikola")
    print("matković")
ispis()
ispis()
def sabiranje(x,y):
    a=x+y
    print(a)
sabiranje(1,2)
def oduzimanje(x,y):
    c=x-y
    return c
d=oduzimanje(4,2)
print(d)
#2 returna
def sabiranje_i_oduzimanje(x,y):
    a=x+y
    b=x-y
    return a,b
rezultat1, rezultat2=sabiranje_i_oduzimanje(3,4)
print(rezultat1, rezultat2)