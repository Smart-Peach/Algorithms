def swap(array, ind1, ind2):
    # print(f"in swap:{array}, {ind1}, {ind2}")
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


def merge_sort(array, start, end):
    # main_middle = good_length(array, start, end)
    main_middle = start + (end - start) // 2
    sort_half(array, start, main_middle, main_middle + 1, main_middle - start)  # Сортируем первую половину массива
    print(main_middle - start)

    # def under_sort(array=array, start=start, end=end):
    # end = main_middle
    while start < end:
        print(f"in while: {start}, {end}")
        middle = start + (main_middle - start) // 2
        print(main_middle)
        length = main_middle - middle - 1
        sort_half(array, middle + 1, main_middle, start, length)
        merge(array, start, middle - 1, main_middle + 1, end, middle + 1)
        print(middle)
        start = 0
        end = middle - 2

    # under_sort(array, start, end)
    # if start < end:
    #     # main_middle = start + (end - start) // 2
    #     # print(f"middle is {main_middle}")
    #     # # Сортируем первую половину массива, используя вторую как буфер
    #     # sort_half(array, start, main_middle, main_middle + 1,
    #     #           main_middle - start)  # Отсортированные числа стоят на arr[middle:end+1]
    #
    #     print(f"after first sort: {arr}")
    #     middle = start + (main_middle - start) // 2
    #     # middle = good_length(array, start, main_middle)
    #     print(f"main_middle: {main_middle}, end: {end}, middle: {middle}")
    #     print(f"for second sort: {array[middle + 1:main_middle + 1]}")
    #
    #     length = main_middle - middle - 1
    #     # length = abs(start - main_middle) + 1
    #
    #     print(f"length is {length}")
    #     sort_half(array, middle + 1, main_middle, start, length)
    #
    #     # print(f"next middle is: {middle}")
    #     print(array)
    #     print(f"for merge: {start}, {middle}, {main_middle + 1}, {end}, {middle + 1}")
    #     merge(array, start, middle - 1, main_middle + 1, end, middle + 1)

    # if start < end:
    #      middle = start + (end - start) // 2
    #
    #     merge_sort(array, start, middle)
    #     merge_sort(array, middle + 1, end)
    #
    #     # buffer = [None] * (end - start + 1)
    #
    #     merge(array, start, middle, middle + 1, end)
    #
    #     for i in range(len(buffer)):
    #         array[start + i] = buffer[i]


arr = [6, 4, 7, 1, 9, 8, 5, 0, 3, 2]
size = len(arr) - 1
merge_sort(arr, 0, size)
print(arr)
