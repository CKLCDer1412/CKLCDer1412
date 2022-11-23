INF = float('inf')
def coinChange(n):
    F = [0] * (n+1)
    for i in range(1, n+1):
        temp = INF
        j = 0
        while j < m and C[j] <= n:
            temp = min(1 + F[n-C[j]], temp)
            j += 1
            F[i] = temp
    return F[n]

C= [int(i)for i in input().split()]
m = len(C)
n=int(input())
print("So tp tien min la:", coinChange(n))