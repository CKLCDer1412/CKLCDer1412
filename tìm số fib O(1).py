def fibonacci(N):
    if N <= 1:
        return N
    first = 0
    second = 1
    for i in range(2, N+1):
        first, second = second, first + second
    return second

N = int(input())
print(fibonacci(N))