def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    Left = [0] * n1
    Right = [0] * n2

    for i in range(n1):
        Left[i] = arr[p + i]

    for j in range(n2):
        Right[j] = arr[q + 1 + j]

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = Right[j]
        j += 1
        k += 1


def mergeSort(arr, p, r):
    if p < r:
        m = (p + (r-1)) // 2
        mergeSort(arr, p, m)
        mergeSort(arr, m+1, r)
        merge(arr, p, m, r)