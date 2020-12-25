from numpy import array, matrix, diagonal
a= array([
[1,2,3,4,5,6],
[7,8,9,10,11,12],
])
print(a.ndim) #dimenzije
print(a.shape) #koliko redova i kolona
b=a.flatten() #pretvara u 1D iz 2D
print(b)
c=b.reshape(3,4) #pretvara u 2d iz 1d
print(c)
print("3D NIZ:")
d=b.reshape(2,2,3) # 3d array, sa 2 2d niza u sebi, svaki po 2 reda i 4 kolone.
print(d)
#rad sa  matrix
e=array([
    [1,2,3,4],
    [5,6,7,8]
])
m=matrix(e)
print(m)
n=matrix("1 2 3; 4 5 6; 7 8 9")
print(n)
print("dijagonalno",diagonal(n)) #ispisuje dijagonalno
print(n.min(), n.max()) #isto što i max(n)
### sabiranje matriksa je isto, ali množenje nije
o=matrix("1 2 3; 4 5 6; 7 8 9")
p=matrix("15 32 35; 42 51 26; 37 98 19")
q=o+p
r=o*p
print(q)
print(r)
