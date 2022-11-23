n=int(input())
l=[int(i) for i in input().split()]
cp=0
while len(l)>1:
    l.sort(reverse = True)
    l[len(l)-2] += l[len(l)-1]
    l.pop()
    cp += l[len(l)-1]
print(cp)
