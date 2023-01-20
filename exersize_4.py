def new(n):
    return [n * i + 2   for i  in  range(n)]
n = 2 
print(new(n))


x = range(2)
t = 2
for i in x:
    v = [t *i]
    print(v)