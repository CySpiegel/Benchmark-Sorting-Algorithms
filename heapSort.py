def heapify(arr, n, i):
    root = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    if leftChild < n and arr[i] < arr[leftChild]:
        root = leftChild

    if rightChild < n and arr[root] < arr[rightChild]:
        root = rightChild

    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, n, root)


def heapSort2(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)