"""B=[int(i)for i in input().split()]
n=B[0]
v=B[1]
A=[]
for i in range(n):
    C=[int(j)for j in input().split()]
    A.append(C)
print(A[0][v-v],A[0][v-3], A[0][v-2],A[0][v-1])
print(A[1][v-v],A[1][v-3],A[1][v-2],A[1][v-1])
print(A[2][v-v],A[2][v-3],A[2][v-2],A[2][v-1])"""

"""l=[]
n=int(input())
for i in range(n):
    a=[int(j) for j in input().split()]
    l.append(a)
for i in range(n):
    for j in range(len(l[i])):
        print(int(l[i][j]), end=" ")
    print()"""

"""l=[]
n=int(input())
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
max=-9999999
min=9999999
for i in l:
    for j in i:
        if j > max:
            max = j
        if j < min:
            min = j
print(max)
print(min)"""

"""l=[]
n=int(input())
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
total = 0
for i in l:
    for j in i:
        if j %2 == 0:
            total += j
print(total)"""


"""Tong tung cot tung hang: l=[]
n=int(input())
v=int(input())
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
for i in range(len(l[0])):
    s=0
    for j in range(n):
        s += l[j][i]
    print(s)
for i in range(n):
    x=0
    for j in range(v):
        x += l[i][j]
    print(x)"""
    

"""l=[]
n=int(input())
v=int(input())
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
for i in range(len(l[0])):
    max = -9999999999999
    for j in range(n):
        if l[j][i] > max:
            max = l[j][i]
    print(max)
for i in range(v):
    min=99999999999
    for j in range(n):
        if l[j][i] < min:
            min = l[j][i]
    print(min)"""
        
import collections     
l=[]
n=int(input())
v=int(input())
count=0
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
l2 = []
for i in l:
    for j in i:
       l2.append(j)

r=collections.Counter(l2)
print(r)

"""l=[]
n=int(input())
for i in range(n):
    a=[int(j)for j in input().split()]
    l.append(a)
for v in l:
    print(v)
    print(sorted(v))"""
