def swap(array, ind1, ind2):
    const = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = const


def merge(arr, start1, end1, start2, end2, buff_start):
    lsize = end1 - start1 + 1
    rsize = end2 - start2 + 1

    print(f"l&r: {arr[start1: end1 + 1]}, {arr[start2: end2 + 1]}")
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
    print(f"in algorithm sort: {array[start:end + 1]}")
    if end - start > 0:
        # if end - start < 3:
        #     insertion_sort(array, start, end)
        # else:
        middle = good_length(start, end)  # Decide where to sort (to the right half)
        # buffer = end - (middle - start - 1) - (end - middle) + 1
        buffer = middle + 1
        if (end - start + 1) % 2 != 0:
            buffer += 1

        print(f"buffer is: {buffer}")
        # print(array[start:end + 1], middle - start)
        # print(f"array is {array}")
        merge_buff_sort(array, start, middle, buffer)  # Sort left half with right half as a buffer
        print(f"after sorting to the right: {array}")
        # if middle - start <= 2:
        #     insertion_sort(array, start, end)
        #     print(f"for insertion: {array[start:middle + 1]}, {array[start:end + 1]}")
        # else:
        rubbish_end = buffer - 1
        # if rubbish_end - start < 3:
        #     print(f"in while: {array[start:rubbish_end + 1]}")
        #     insertion_sort(array, start, end)
        #     print(f"after sorting rubbish: {array}")
        # else:
        while rubbish_end - start > 2:
            print(f"in while: {array[start:rubbish_end + 1]}")
            rubbish_middle = good_length(start, rubbish_end)
            merge_buff_sort(array, rubbish_middle, rubbish_end, start)  # Sort right "rubbish half" to the left half
            merge(array, start, rubbish_middle, rubbish_end + 1, end, rubbish_middle + 1)
            print(f"after sorting rubbish: {array}")
            rubbish_end = rubbish_middle
            print(f"end is {rubbish_end} and start is {start}")
        insertion_sort(array, start, end)


def merge_buff_sort(array, start, end, buff):
    print(f"in merge_sort: {array[start: end + 1]}, {buff}")
    if start < end:
        middle = start + (end - start) // 2
        algorithm_sort(array, start, middle)
        algorithm_sort(array, middle + 1, end)
        merge(array, start, middle, middle + 1, end, buff)


def start(arr):
    size = len(arr) - 1
    algorithm_sort(arr, 0, size)
    print(arr)
    # Recursion stops earlier than needed (artificial step) etc. [8, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]
    # insertion_sort(arr, 0, size)


# arr = [13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]
start(arr)
print(arr)
