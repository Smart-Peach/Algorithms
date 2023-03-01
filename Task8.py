def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    b, c = [], []
    for i in range(n1):
        b.append(a[p + i])
    for j in range(n2):
        c.append(a[q + j + 1])

    count_gl = 0
    i, j = 0, 0
    k = p
    while i < n1 and j < n2:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
            count_gl += len(b) - i
        k += 1
    while i < n1:
        a[k] = b[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = c[j]
        k += 1
        j += 1
        count_gl += len(b) - i
    return count_gl


def merge_sort(array, p, r) -> int:
    res_gl = 0
    if p < r:
        q = (p + r) // 2
        res_gl += merge_sort(array, p, q)
        res_gl += merge_sort(array, q + 1, r)
        res_gl += merge(array, p, q, r)
    return res_gl


def count_local_inversions(array):
    count = 0
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            count += 1
    return count


def inversions(arr):
    local_inversions = count_local_inversions(arr)
    global_inversions = merge_sort(arr, 0, len(arr) - 1)
    if global_inversions == local_inversions:
        return True
    return False


l = [1, 2, 0]
size = len(l) - 1
print(inversions(l))
