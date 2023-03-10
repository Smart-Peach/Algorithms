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
    for j in range(start, end + 1):
        key = arr[j]
        i = j - 1
        while i >= start and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


def sort_half(array, start, end, buff_start, initial_length):
    # print(f" halfed array: {array[start: end + 1]}")
    # print(f"initial length: {initial_length}, start-end: {start - end}")
    if start < end:
        middle = start + (end - start) // 2

        sort_half(array, start, middle, buff_start, initial_length)
        sort_half(array, middle + 1, end, buff_start, initial_length)

        merge(array, start, middle, middle + 1, end, buff_start)

        # print(f"after swapping: {array}")
        # print(start, end, buff_start)

        # Чтобы нормально сортировалось, я передвигаю числа из буффера обратно в массив,
        # но в последней итерации этого делать не надо
        # print(start, end, buff_start)
        # if start != 0 or end != buff_start - 1:

        print(f"initial length: {initial_length}, start-end: {abs(start - end)}")
        if abs(end - start) != initial_length:
            for i in range(end - start + 1):
                swap(array, start + i, buff_start + i)
            # array[start + i] = buffer[i]
        # print(f"array after merge: {array}")


def good_length(start, end):
    middle = start + (end - start) // 2
    if (end - start) % 2 != 0:
        middle -= 1
    return middle


def merge_sort1(array, start, end):
    # main_middle = good_length(array, start, end)
    main_middle = start + (end - start) // 2
    sort_half(array, start, main_middle, main_middle + 1, main_middle - start)  # Сортируем первую половину массива
    # print(main_middle - start)

    # def under_sort(array=array, start=start, end=end):
    print(f"after first sort: {array}")
    end = main_middle
    while start < end:
        print(f"in while: {start}, {end}")
        middle = start + (end - start) // 2
        length = end - middle - 1
        sort_half(array, middle + 1, end, start, length)
        print(f"one more sort: {array}")
        merge(array, start, middle - 1, end + 1, end,
              middle + 1)  # Мердж не работает, просто ставит рядом отсортированные массивы (пАчИмУ?!?!?!?)
        print(f"merging: {array}")
        print(middle)
        start = 0
        end = middle


def merge_left(array, start, end, buff_start):
    print(f"in merge_left: {array[start:end + 1]}, {buff_start}")
    if start < end:
        middle = start + (end - start) // 2

        merge_left(array, start, middle, start - 1)
        merge_left(array, middle + 1, end, start - 1)
        merge(array, start, middle, middle + 1, end, buff_start)


def merge_sort(array, start, end):
    # middle = start + (end - start) // 2
    print(f"array at entrance: {array[start:end + 1]}")
    if start < end:
        if end - start < 3:
            insertion_sort(array, start, end)
        else:
            middle = start + (end - start) // 2
            buff_start = end + 1

            merge_sort(array, start, middle)
            merge_sort(array, middle + 1, end)
            merge(array, start, middle, middle + 1, end, buff_start)
            print(start, end, buff_start)
            print(f"after one merge: {array}")

            unsorted_middle = (end - start) // 2 + 1
            merge_left(array, unsorted_middle, buff_start - 1, start)
            print(f"after sort to the left: {array}")
            print(f"before big merge: {start}, {unsorted_middle - 1}, {buff_start}, {end * 2 + 1}")
            merge(array, start, unsorted_middle - 1, buff_start, end * 2 + 1, unsorted_middle)
            print(f"after merge two sorted arrays: {array}")
            merge_sort(array, start, unsorted_middle - 1)
            merge(array, start, unsorted_middle - 1, unsorted_middle, end * 2 + 1, end * 2 + 2)
            f = 1
            print(f"should be lafsorted: {array}, {start}, {end}")


arr = [13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60]
size = len(arr) - 1
merge_sort(arr, 0, size)
print(arr)
