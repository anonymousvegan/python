def generator():
    yield 5           #umesto return koristimo yield, vraća je kao iterator:
    yield 1
    yield 3
    yield 9
a=generator()
print(a)
print(a.__next__())
for i in a:
    print(i)
def kvadrat():
    n=1
    while n<=10:
        kvadrat=n*n
        yield kvadrat
        n+=1
k=kvadrat()
for i in k:
    print(i)