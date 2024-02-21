def gen(n):
    for i in range(0, n+1):
        yield n-i
a = int(input())
g = gen(a)
for i in g:
    print(i)