my_array = [7, 12, 9, 4, 11]


# Lowest number in an array
def findLowest(arr):
    lowest = arr[0]

    for x in arr:
        if x < lowest:
            lowest = x

    return lowest


print("Lowest value:", findLowest(my_array))


# Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print("Bubble Sort:", bubbleSort([7, 12, 9, 4, 11]))


# Selection Sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print("Selection Sort:", selectionSort([7, 12, 9, 4, 11]))


# Insertion Sort
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        curr_value = arr[i]
        j = i - 1

        while j >= 0 and curr_value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr_value

    return arr


print("Insertion Sort:", insertionSort([64, 34, 25, 12, 22, 11, 90, 5]))


# Quick Sort
def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            arr[low], arr[j] = arr[j], arr[low]
            low += 1

    arr[low], arr[high] = arr[high], arr[low]

    return low


print("Quick Sort:", quickSort([11, 9, 12, 7, 3]))

# Merge Sort


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("Merge Sort:", mergeSort([12, 8, 9, 3, 11, 5, 4]))
