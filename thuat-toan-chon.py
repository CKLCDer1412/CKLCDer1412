"""arr=[int(i)for i in input().split()]
m=[]
for q in range(len(arr)):
    min_index = q
    for j in range(q +1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[q], arr[min_index] = arr[min_index], arr[q]
print(arr)"""

arr=[int(i)for i in input().split()]
for j in range(len(arr)-1):
    for q in range(j+1, len(arr)):
        if arr[q] < arr[j]:
            arr[q], arr[j] = arr[j], arr[q]
for k in arr:
    print(k, end= " ")