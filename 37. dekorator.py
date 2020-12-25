def oduzimanje(a,b):                    #1. def funkcije 
    print(a-b)                     #11 izračunava
def pametno_oduzimanje(funkcija): #2def funkciju 4. poprima parametar funkciju 
    def zamena(a,b):              # 5. definiše zamenu sa  dva parametra a b
        if a<b:                   #8.ako je a<b
            a,b=b,a               #9 zameni
        return funkcija(a,b)      #v10. raća funkcija(a,b)
    return zamena                #7, vraća zamenu=10
novo=pametno_oduzimanje(oduzimanje) #3. novo=pametno(obično)
novo(2,5)                           #6. prima parametre 2 i 5
###NOVO PRIMA FUNKCIJU PAMETNO ODUZIMANJE SA PARAMETROM OUZIMANJE.
###VRAĆA FUNKCIJU ODUZIMANJE SA PARAMETROM A I B  NAKON PROVERE I ZAMENE.