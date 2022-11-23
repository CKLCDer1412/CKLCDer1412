C= ["A", "B", "C"]
def Hanoi(n, i, j, k):
    if n > 0:
        Hanoi(n-1, i, k, j)
        print("chuyển đĩa", n, 'từ cọc', C[i], 'sang cọc', C[j])
        Hanoi(n-1,k,j,i)
        
n, i, k, j = [int(q)for q in input().split()]
Hanoi(n, i, k, j)