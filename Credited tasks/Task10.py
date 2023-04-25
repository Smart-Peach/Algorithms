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
        if b[i] <= c[j]:
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


def merge_sort_start(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_start(array, p, q)
        merge_sort_start(array, q + 1, r)
        merge(array, p, q, r)


def merge_sort(array):
    size = len(array) - 1
    merge_sort_start(array, 0, size)
    return array


def counting_sort(arr, elem_ind):
    m = (max(arr, key=lambda x: x[elem_ind]))[elem_ind]
    counter = [0] * (ord(m) + 1)
    for i in arr:
        counter[ord(i[elem_ind])] += 1

    for i in range(len(counter) - 1):
        counter[i + 1] += counter[i]

    res = [0] * len(arr)
    for i in reversed(arr):
        res[counter[ord(i[elem_ind])] - 1] = i
        counter[ord(i[elem_ind])] -= 1
    return res


def lsd_radix_sort(arr_str):
    if len(arr_str) == 0:
        return arr_str
    symbols = len(arr_str[0])
    for i in reversed(range(symbols)):
        arr_str = counting_sort(arr_str, i)
    return arr_str

