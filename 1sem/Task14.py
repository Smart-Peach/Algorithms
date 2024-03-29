import random


def swap(array, ind1, ind2):
    const = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = const


def partition(array, start, end, pivot):
    if pivot != start:  # if it isn't first swap
        swap(array, start, pivot)

    i = j = start + 1
    while j != end + 1:
        if array[j] < array[start]:
            swap(array, j, i)
            i += 1
        j += 1

    swap(array, i - 1, start)
    return i - 1


def kth(array, start: int, end: int, k: int) -> int:

    if end - start == 0:
        return array[start]

    pivot = random.randint(start, end)
    p = partition(array, start, end, pivot)

    if p + 1 == k:
        return array[p]
    elif p + 1 > k:
        return kth(array, start, p, k)
    else:
        return kth(array, p + 1, end, k)


nums = [-1, -1]
k = 2
k = len(nums) - k + 1
size = len(nums) - 1
print(kth(nums, 0, size, k))
