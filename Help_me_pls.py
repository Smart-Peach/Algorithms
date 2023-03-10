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
            # print(buff_start + k, start1 + i)
            swap(arr, buff_start + k, start1 + i)
            k += 1
            i += 1
        else:
            # print(buff_start + k, start2 + j)
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
    print(f"insertion: {start}, {end}")
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


def smart_sort(array, start, end):
    # middle = start + (end - start) // 2  # Decide where to sort (to the right half)
    middle = good_length(start, end)
    print(1)
    merge_sort(array, start, middle, middle + 1)  # Sort left half with right half as a buffer
    print(f"first sort: {array}, {middle - start}")
    if middle - start < 2:
        insertion_sort(array, start, end)
        print(f"rubbish to the right {array}")
    else:
        sub_end = middle
        while sub_end - start > 2:
            print(f"in while: {start}, {sub_end}")
            # rubbish_middle = middle // 2  # Choose another buffer (for sorting rubbish at the left)
            # rubbish_middle = start + (sub_end - start) // 2
            rubbish_middle = good_length(start, sub_end)
            print(rubbish_middle)
            # merge_sort(array, rubbish_middle + 1, sub_end, start)  # Sort right "rubbish half" to the left half
            merge_sort(array, rubbish_middle, sub_end, start)  # Sort right "rubbish half" to the left half
            print(f"rubbish to the right {array}")
            print(f"buffer: {rubbish_middle + 1}")
            merge(array, start, rubbish_middle, sub_end + 1, end, rubbish_middle + 1)
            print(f"merging: {array}")
            sub_end = rubbish_middle


def merge_sort(array, start, end, buff):
    print(f"in merge_sort: {array[start: end + 1]}, {buff}")
    if start < end:
        middle = start + (end - start) // 2
        smart_sort(array, start, middle)
        smart_sort(array, middle + 1, end)
        merge(array, start, middle, middle + 1, end, buff)


def start_sort(arr):
    size = len(arr) - 1
    smart_sort(arr, 0, size)
    insertion_sort(arr, 0, size)


# arr = [13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]
start_sort(arr)
print(arr)
