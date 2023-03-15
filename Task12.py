import random


def swap(array, ind1, ind2):
    const = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = const


def quick_sort(array, start, end):
    if end - start > 0:
        elem_ind = random.randint(start, end)  # Choose random element (index)
        if elem_ind != start:  # if it isn't first swap
            swap(array, start, elem_ind)

        i = j = start + 1
        while j != end + 1:
            if array[j] <= array[start]:
                swap(array, j, i)
                i += 1
            j += 1

        swap(array, i - 1, start)
        quick_sort(array, start, i - 2)
        quick_sort(array, i, end)


arr = [5, 2, 7, 8, 435, 3, 7, 7, 35, 67, 576, 3, 667, 56, 4]
size = len(arr) - 1
quick_sort(arr, 0, size)
print(arr)
