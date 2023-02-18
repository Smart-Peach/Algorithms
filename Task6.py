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


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def special_sort(list):
    merge_sort(list, 0, len(list) - 1)
    middle = len(list) // 2
    result = []
    for i in range(middle):
        result.append(list[i])
        result.append(list[i + middle])
    return result


l = [1, 3, 2, 2, 3, 1]
print(special_sort(l))
