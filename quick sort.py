def partition(a, left, right):
    p =right
    pivot = a[p]
    i = left -1
    for j in range(left, right):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[p],a[i+1]=a[i+1],a[p]
    return i+1
def quicksort(a, left, right):
    if left < right:
        p = partition(a, left, right)
        quicksort(a, left, p-1)
        quicksort(a, p+1, right)

a=[int(i)for i in input().split()]
quicksort(a, 0, len(a)-1)
print(a)
