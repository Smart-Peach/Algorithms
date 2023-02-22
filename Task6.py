def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    b, c = [], []
    for i in range(n1):
        b.append(a[p + i])
    for j in range(n2):
        c.append(a[q + j + 1])
    i, j = 0, 0
    k = p
    while i < n1 and j < n2:
        if b[i] >= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = b[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = c[j]
        k += 1
        j += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
    return a


def wiggle_sort(nums):
    arr = merge_sort(nums, 0, len(nums) - 1)  # отсортированный
    middle = len(nums) // 2
    arr_greater, arr_less = arr[:middle], arr[middle:]  # Делим на два массива
    k, j = 0, 0
    for i in range(len(arr)):
        if i % 2 == 0:
            nums[i] = arr_less[k]
            k += 1
        else:
            nums[i] = arr_greater[j]
            j += 1


l = [5, 5, 5, 4, 4, 4, 4]
wiggle_sort(l)
print(l)
