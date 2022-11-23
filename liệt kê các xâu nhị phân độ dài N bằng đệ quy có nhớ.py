s=[]
def tried(i):
    if len(s) == n:
        print(s)
    else:
        for i in range(2):
            s.append(i)
            tried(i+1)
            s.pop()

n=int(input())
tried(0)