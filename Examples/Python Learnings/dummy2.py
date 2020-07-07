def test(n):
    while n>0:
        yield n
        n-=1
    raise StopIteration

for x in test(10):
    print(x)