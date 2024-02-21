def even(n):
    for i in range(0, n+1):
        if i%2 == 0:
            yield i
a = int(input())
g = even(a)
for i in g:
    print(i)