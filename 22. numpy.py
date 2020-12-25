#glavna upotreba numpy-a je 2d array
import numpy as np
niz= np.array([1,2,3,4], "i")
print(niz)
niz2=np.array([2,3,4,5]) #ne mora se pisati "i" sa numpy.
print(niz2)
a=[1,2,3,4]
### MULTIDIMENZIONALNI NIZ
x = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]], np.int32) ## CD
print(x) 
y=np.array([
    [[1, 2, 3], [4, 5, 6], [7,8,9]],
     [[10 ,11, 12], [13, 14, 15], [16,17,18]],
      [[19, 20, 21], [22, 23, 24], [25,26,27]] 
      ])
print(y)
print(y[2][2][2]) #index starta od 0! 
