a=1
b=2
c=a+b
a=a+3
b+=4
print(a,b,c)
d=a**b
print(d)
e=5
f=6
g,h=7,8 ###dodela vrednosti u jednoj liniji koda!
print(g,h) 
n=10
print(n)
n=-n
print(n)
n=-n ####minus i minus daju +
print(n) 
n=-n #sada je -10
n=+n #+ i minus daju -
print(n)
j=4
k=3
m=j<k #false
print(m)
####ovde postoje i operatori <, >, <=, >=, ==, !=, realno znam ih pa mi mučno da ih sve isprobavam.
###logički operatori su and, or, not!
z=10
print(z<20 and z > 15) #false
print(z<20 or z > 5)  #true
y= z<5 #false
x = not y
print(y,x) # true