def gen(n):
    for i in range(0, n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
a = int(input())
g = gen(a)
for i in g:
    print(i)