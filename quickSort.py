def partition(A, p, r):
    i = p - 1
    pivot = A[r]
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            # print(A)
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickSort(A, p, r):
    if p < r:
        # print('Pivot index', r, 'Value ', A[r], A)
        q = partition(A, p, r)
        # print("Upper", r)
        quickSort(A, p, q - 1)
        # print("Lower", r)
        quickSort(A, q + 1, r)