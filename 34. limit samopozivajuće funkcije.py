import sys
print(sys.getrecursionlimit()) ##ograničenje samopozivajuće funkcije je 1000, nije beskonačno
sys.setrecursionlimit(100) ##otprilike
i=0
def poz():
    global i
    i=i+1
    print(i)
    poz()
poz()