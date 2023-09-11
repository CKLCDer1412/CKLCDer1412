n=int(input())
s=[int(i) for i in input().split()]
f=[int(i) for i in input().split()]
l=[]
kq=[]
for i in range(len(s)):
    b=[s[i], f[i], i+1]
    l.append(b)
l=sorted(l, key=lambda x:x[1], reverse=False)
kq.append(l[0])
for j in range(1, n):
    if l[j][0]>=kq[len(kq)-1][1]:
        kq.append(l[j])
for x in kq:
    print(x[2], end=' ')
print("hello world")

    
 


    

