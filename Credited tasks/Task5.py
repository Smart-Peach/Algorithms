def insertion_sort_k(arr, start, k):
    for j in range(start, len(arr), k):
        key = arr[j]
        i = j - k
        while i >= 0 and arr[i] < key:
            arr[i + k] = arr[i]
            i -= k
        arr[i + k] = key


def shell_sort(arr):
    size = len(arr)
    k = i = 0
    sub_arr_len = []
    while k < size:
        k = (3 ** i - 1) // 2
        i += 1
        sub_arr_len.insert(0, k)
    sub_arr_len.pop(0)

    for k in sub_arr_len:
        for start in range(k):
            insertion_sort_k(arr, start, k)


def hIndex(citations):
    if len(citations) == 1:
        return 0 if citations[0] == 0 else 1
    shell_sort(citations)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return i
        if i + 1 == len(citations):
            return i + 1


list = [3, 0, 6, 1, 5]
print(hIndex(list))
