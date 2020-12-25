brojevi=[1,2,3,4,5]
#print(brojevi[0]) #prvi način 
#print(brojevi[1])
#print(brojevi[2])
#print(brojevi[3])
#print(brojevi[4]) #### ako napišemo 5 kao index neće raditi
#for i in brojevi: #drugi način! 
#    print(i)
#način prvi     #################
it = iter(brojevi)
print(it.__next__())
print(it.__next__())
print(next(it))   #isto 
#sam pravim iterator
class odjedandodeset:
    def __init__(self):
        self.n=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<10:
            val=self.n
            self.n +=1
            return val
        else:
            raise StopIteration ##############33jedino ovako može da se zaustavi loop.
value=odjedandodeset()
print(value.__iter__())
for i in value:
    print(i)