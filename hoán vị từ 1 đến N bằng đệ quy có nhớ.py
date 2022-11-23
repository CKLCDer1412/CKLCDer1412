n=int(input())
check=[False]*(n+1)
a=[]
def backtrack(i):
    if len(a) == n:
        print(*a)
    else:
        for j in range(1, n+1):
            if check[j] == False:
                a.append(j)
                check[j] = True
                backtrack(i+1)
                check[j] = False
                a.pop()

backtrack(n)