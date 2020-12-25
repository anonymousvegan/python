i=0
while i<=10:
    print("nikola ", end="")  # bez nove linije
    i+=1
print("gotovo") 
a=1
while a<=5:
    b=1
    print("pas ",end="")
    while b<=5:
        print("pućko ",end="")
        b+=1
    print()
    a+=1
print("finiš")
imena=["nikola", "miroljub", "skenderbeg"]
for i in imena:
    print(i)
ime="nikola"
for i in ime:
    print(i)
for i in range(10):
    print(i) ### 0 1 2 3 4 5 6 7 8 9 
for i in range(10,0, -1): ##unazad
    print(i, end="") ### 10987654321
for i in range(100):
    if i%10!=0:  #preskače 10, 20...
        print(i)
