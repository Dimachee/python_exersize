def  new(n):
    return   n[len(n)- 2] in n[len(n) -1]  and n[len(n)- 2] != n[len(n)- 1] 
n = ["asd", "dsada", "fd", "fdddddd"]
print(new(n))