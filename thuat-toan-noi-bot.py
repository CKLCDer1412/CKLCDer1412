"""a=[int(j)for j in input().split()]
for i in range(len(a)-2,-1,-1):
    v=i
    while a[v] > a[v+1]:
        a[v],a[v+1] = a[v+1],a[v]
        v+=1
        if a
        if a[v] < a[v+1]:
            break
    print(a[v], end=" ")"""

a=[int(i)for i in input().split()]
n=len(a)
swap = False
for j in range(n-1):
    for v in range(0, n-j-1):
        if a[v] > a[v+1]:
            swap = True
            a[v],a[v+1] = a[v+1],a[v]
    if not swap:
        break
for j in range(len(a)):
    print( a[j], end=" ")
    