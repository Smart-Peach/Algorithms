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


l = [5, 6, 78, 0, 1, 89, 25, 4, 6, 8]
size = len(l) - 1
merge_sort(l, 0, size)
print(l)
