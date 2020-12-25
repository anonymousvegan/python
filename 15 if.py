x= input("unesi broj")
broj=int(x)
if broj%2==0:
    print("broj je paran")
    if broj<10:
        print("malo")
    elif broj<15 and broj>10:
        print("srednje")
    else: 
        print("veliko")
else: 
    print("broj je neparan")
## može se pisati i ovako
if(1<10):
    print("istina")