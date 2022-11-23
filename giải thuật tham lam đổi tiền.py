ds = [int(dsi)for dsi in input().split()]
ds.sort(reverse= True)
n = int(input())
for i in ds:
    if i <= n:
        print("Số tờ: ", i, ": ", n//i)
        n = n % i