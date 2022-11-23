def LIS(A):
    n = len(A)
    p = [None]*n
    L = [1] * n
    for k in range(n):
        maxL = 1
        Idx = None
        for  i in range(k):
            if A[i] < A[k] and maxL < L[i] +1:
                maxL = L[i] + 1
                Idx = i
        L[k] = maxL
        p[k] = Idx
    maxL = L[0]
    Idx = 0
    for k in range(n):
        if L[k] > maxL:
            maxL = L[k]
            Idx = k
    return Idx, maxL, p, L
def showLIS(Idx, p):
    q=[]
    while Idx != None:
        q.append(Idx)
        Idx = p[Idx]
    for i in range(len(q)-1, -1, -1):
        print(A[q[i]], end=" ")
        
A=[int(i)for i in input().split()]
Idx, maxL, p, L= LIS(A)
print(Idx, maxL)
showLIS(Idx, p)


"""def LIS_new(A):
    n = len(A)
    I = [None]*n
    S = [None] * n
    L=0
    S[0] = A[0]
    I[0] = 0
    p=[None] *n
    for i in range(n):
        if A[i] <= S[0]:
            S[0] = A[i]
            I[0] = i
            p[i] = None
        elif S[L] < A[i]:
            L += 1
            S[L] = A[i]
            I[L] = i
            p[i] = I[L-1]
        else:
            left = 0
            right = L
            while left < right - 1:
                mid = (left+right)//2
                if S[mid] <= A[i]:
                    left = mid
                else:
                    right = mid
            k = right
            S[k] = A[i]
            I[k] = i
            p[i] = I[k-1]
    return L,I,p
def showLIS(L, I, p):
    q=[]
    while L != None:
        q.append(L)
        L = p[L]
    for i in range(len(q)-1, -1, -1):
        print(A[q[i]], end=" ")
        
A=[int(i)for i in input().split()]
L, I, p= LIS_new(A)
showLIS(L,I,p)"""