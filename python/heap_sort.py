def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if the left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if the right child exists and is greater than the largest element
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest element is not the root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap from the given list
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap

# Example
arr = [7, 3, 8, 11, 35, 83, 1]
heap_sort(arr)
print("Sorted array:", arr)
