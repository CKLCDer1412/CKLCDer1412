a=[]
n=int(input())
check=[False]*(n+1)
def kt(d):
    for i in range(len(d)-1):
        if d[i] +1 == d[i+1] or d[i]-1 == d[i+1]:
            return False
            break
    return True

def hoanvi(i):
    if len(a) == n:
        if kt(a) == True:
            for x in range(len(a)):
                print(f'{x+1}:{a[x]}', end=" ")
                print()
    else:
        for j in range(1, n+1):
            if check[j] == False:
                a.append(j)
                check[j] = True
                hoanvi(i+1)
                check[j] = False
                a.pop()

hoanvi(0)