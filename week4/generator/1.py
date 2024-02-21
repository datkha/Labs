def squares(n):
    for i in range(1, n+1):
        yield i**2

a = int(input())

g = squares(a)
for i in g:
    print(i)