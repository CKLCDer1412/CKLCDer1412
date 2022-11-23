def coso_10_sang_2(x):
    i=0
    ds=''
    while x != 0:
        i = x % 2
        ds+=str(i)
        x=x//2
    print(str(ds)[::-1])
    
x=int(input())
coso_10_sang_2(x)