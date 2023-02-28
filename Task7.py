def merge(arr, start1, end1, start2, end2):
    lsize = end1 - start1 + 1
    rsize = end2 - start2 + 1
    i = j = 0
    while i < lsize and j < rsize:
        if arr[start1 + i] <= arr[start2 + j]:
            i += 1
            # res[k] = arr[start1 + i]
            # k += 1
            # i += 1
        else:
            val = arr[start2 + j]
            place = start2 + j

            while place != (start1 + i):
                arr[place] = arr[place - 1]
                place -= 1
            arr[start1 + i] = val

            i += 1
            lsize += 1
            j += 1
            # res[k] = arr[start2 + j]
            # k += 1
            # j += 1

    # while i < lsize:
    #     res[k] = arr[start1 + i]
    #     k += 1
    #     i += 1
    # while j < rsize:
    #     res[k] = arr[start2 + j]
    #     k += 1
    #     j += 1


def merge_sort(array, start, end):
    if start < end:
        middle = start + (end - start) // 2

        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)

        # buffer = [None] * (end - start + 1)

        merge(array, start, middle, middle + 1, end)

        # for i in range(len(buffer)):
        #     array[start + i] = buffer[i]


arr = [5, 2, 3, 1]
size = len(arr) - 1
merge_sort(arr, 0, size)
print(arr)
