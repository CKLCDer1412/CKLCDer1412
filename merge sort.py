def mergeSort(A, left, right):
    if left < right:
        mid = (left + right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        B = A.copy()
        i =left
        j = mid+1
        k = left
        while i <= mid and j <= right:
            if A[i] < A[j]:
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                j += 1
            k += 1
        if i > mid:
            while j <= right:
                B[k] = A[j]
                j += 1
                k += 1
        else:
            while i <= mid:
                B[k] = A[i]
                i += 1
                k += 1
        A[left:right+1]= B [left:right+1]
        
A= [int(i)for i in input().split()]
mergeSort(A, 0, len(A)-1)
print(A)