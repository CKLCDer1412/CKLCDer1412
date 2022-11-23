def climbStairs(n, mem=dict()):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if mem.get(n, 0) == 0:
        mem[n] = climbStairs(n-1, mem) + climbStairs(n-2, mem)
    return mem[n]
    
n=int(input())
print(climbStairs(n))