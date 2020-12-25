#tuple je isto što i lista samo je konstantno.
#brže radi od liste, zato se koristi.
tup=(1,2,2,2,3,4)
print(tup)
print(tup[5])
print(tup.count(2))
print(tup.index(1))
tup=(6,7,8) #možemo menjati ceo niz, ali ne i  pojedinačan indeks.
print(tup)
skup={1,3,4,5,6,3,5,7} #ne ponavljaju se vrednosti
#NE MOŽE SE KORISTITI INDEX, OVO JE  SET
print(skup)
skup.add(45)  #dodaje 45 
print(skup)
skup.clear() #briše sve 
print(skup)
skup ={2,3,4,5}
print(skup)
skup2={3,4,5,6}
print(skup.difference(skup2))
print(skup2.difference(skup))
skup3=skup.difference(skup2) ## ovo će naći razliku, ali 1 i 2 ostaju isti
skup.difference_update(skup2) ## ovo će promeniti skup u njegovu razliku
print("razlika",skup)
skup={"a","b","c"}
skup.discard("c") #briše c iz skupa.
print(skup)
skup={"a","b","c"}
skup2={"b","c","d"}
skup3={"b","f","g"}
print(skup.intersection(skup2)) #presek (b,c)
print(skup.intersection(skup2,skup3)) #presek (b)
print(skup&skup2&skup3) #radi istu stvar i operator &
skup.intersection_update(skup2) #skup će biti jednak preseku, skup 2 se ne menja
print(skup, skup2)
skup={1,2,3}
skup2={4,5,6}
print(skup.isdisjoint(skup2)) # da li su različiti?
skup={1,2,3,4,5,6}
print(skup2.issubset(skup))
print(skup.issuperset(skup2))
skup.pop() #nasumično briše 1 element.
print(skup)
skup={1,2,3,4,5,6}
skup.remove(6) #briše 6
print(skup)
skup2={4,5,6,7,8,9,10}
print(skup.symmetric_difference(skup2)) #  a unija b razlika presek
skup.symmetric_difference_update(skup2)
print(skup,skup2)
skup={1,2,3}
print(skup.union(skup2)) #unija 2 skupa
skup2={4,5,6}
print(skup.update(skup2)) #skup1 će biti 123456, sama funkcija vraća none
print(skup)
skup3={7,8,9}
print(min(skup3))
print(max(skup3))