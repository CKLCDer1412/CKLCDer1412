def coso_2_sang_10(x):
    t=0
    for i in range(len(x)):
        if x[i]=="1":
            t=t+2**((len(x)-1)-i)
    print(t)

x=input()
coso_2_sang_10(x)