def swap(array, ind1, ind2):
    const = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = const


def merge(arr, start1, end1, start2, end2, buff_start):
    lsize = end1 - start1 + 1
    rsize = end2 - start2 + 1

    i = j = k = 0
    while i < lsize and j < rsize:
        if arr[start1 + i] <= arr[start2 + j]:
            swap(arr, buff_start + k, start1 + i)
            k += 1
            i += 1
        else:
            swap(arr, buff_start + k, start2 + j)
            k += 1
            j += 1

    while i < lsize:
        swap(arr, buff_start + k, start1 + i)
        k += 1
        i += 1
    while j < rsize:
        swap(arr, buff_start + k, start2 + j)
        k += 1
        j += 1


def insertion_sort(arr, start, end):
    for j in range(start, end + 1):
        key = arr[j]
        i = j - 1
        while i >= start and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


def good_length(start, end):
    middle = start + (end - start) // 2
    if (end - start + 1) % 2 != 0:
        middle -= 1
    return middle


def algorithm_sort(array, start, end):
    if end - start > 0:
        middle = good_length(start, end)  # Decide where to sort (to the right half)

        buffer = middle + 1  # Choose buffer
        if (end - start + 1) % 2 != 0:
            buffer += 1

        merge_buff_sort(array, start, middle, buffer)  # Sort left half with right half as a buffer
        rubbish_end = buffer - 1

        # Sort rubbish at the left
        while rubbish_end - start > 2:
            rubbish_middle = good_length(start, rubbish_end)
            merge_buff_sort(array, rubbish_middle, rubbish_end, start)  # Sort right "rubbish half" to the left half
            merge(array, start, rubbish_middle, rubbish_end + 1, end, rubbish_middle + 1)
            rubbish_end = rubbish_middle
        insertion_sort(array, start, end)  # When two elements left in rubbish do insertion sort


def merge_buff_sort(array, start, end, buff):
    if start < end:
        middle = start + (end - start) // 2
        algorithm_sort(array, start, middle)
        algorithm_sort(array, middle + 1, end)
        merge(array, start, middle, middle + 1, end, buff)


def start(arr):
    size = len(arr) - 1
    algorithm_sort(arr, 0, size)


# arr = [13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]
start(arr)
print(arr)
