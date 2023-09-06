"""Merge sort like in DMTA lectures"""


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


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


"""Counting sort sorts absolutes"""


def counting_sort(arr):
    counter = [0] * (max(arr) + 1)
    for i in arr:
        counter[abs(i)] += 1
    for i in range(len(counter) - 1):
        counter[i + 1] += counter[i]
    res = [0] * len(arr)
    for i in reversed(arr):
        res[counter[abs(i)] - 1] = i
        counter[abs(i)] -= 1
    return res
