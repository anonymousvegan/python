def ispisi(n):
    a=0
    b=1
    if n>0:
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c=a+b
                print(c)
                a=b
                b=c
    else:
        print("pogrešan broj,unesite ponovo")
n=int(input())
ispisi(n)