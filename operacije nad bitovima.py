komplement=~5 ### -6
######### ako kontam,kompement od 
######### 5 i drugi komp od 6
######### treba da se poklapaju
######### 0 0 0 0 0 1 0 1 #####ovo je 5
########  1 1 1 1 1 0 1 0 ##### ovo je comp od 5
########  0 0 0 0 0 1 1 0 ####6

########  1 1 1 1 1 0 0 1 ##1. komp od 6
######+1  1 1 1 1 1 0 1 0 ##2. komp od 6 jednako kao gore!
######## znači, prvi komplement od 5 jednak je drugom komplementu od -6, zato dobijam -6!
print(komplement)
logickoi= 12&4 
##### 0 0 0 0 1 1 0 0
##### 0 0 0 0 0 1 0 0
#oba1 0 0 0 0 0 1 0 0 ##4
print(logickoi)   ### 4
logickoili= 5|8
##### 0 0 0 0 0 1 0 1
##### 0 0 0 0 1 0 0 0
#1 1# 0 0 0 0 1 1 0 1 ##13
print(logickoili)
##XOR
XOR= 4^5
#### 0 0 0 0 0 1 0 0
#### 0 0 0 0 0 1 0 1
#raz 0 0 0 0 0 0 0 1   #1
print(XOR)
##### left i right shift
#####  m << n
#### broj m se pretovir u binarni format, doda mu se zarez i beskonačno nula
#### broj se zatim pomera  za n mesta u levo, odnosno dopisuje  mu se  n nula
leftshift= 15 << 3
#### 0 0 0 0 1 1 1 1
#### 0 0 0 0 1 1 1 1, 0 0 0 0 (pomeramo 3 nule iza zareza)
#### 0 1 1 1 1 0 0 0, 0
#### 0 1 1 1 1 0 0 0          #### 120
print(leftshift)
#### right shift radi isto, samo u desno, stim što se vrednosti iza zareza ne računaju
#### m >> n , broj m se pretvara u binarni  i briše mu se zadnjih n broj cifara
rightshift=10>>1 
####  0 0 0 0 1 0 1 0 , 0 0 0 0 
####  0 0 0 0 1 0 1, 0 0 0 0 0 ### 5
print(rightshift)
##### drago mi je da je ovo gotovo, najteža lekcija do sad