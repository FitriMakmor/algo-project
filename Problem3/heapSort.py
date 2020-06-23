def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # smaller than root
    if l < n and arr[i].score > arr[l].score:
        smallest = l

    # See if right child of root exists and is
    # smaller than root
    if r < n and arr[smallest].score > arr[r].score:
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

    # Heapify the root.
        heapify(arr, n, smallest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Driver code to test above
#
#
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d" % arr[i]),
