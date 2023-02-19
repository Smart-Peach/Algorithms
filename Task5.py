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
    sub_arr_len = int((2 * size + 1) ** (1/3))
    flag = 1
    while sub_arr_len > 0 and flag:
        if sub_arr_len == 1:
            flag = 0
        for start in range(sub_arr_len):
            insertion_sort_k(arr, start, sub_arr_len)
        sub_arr_len = int((2 * sub_arr_len + 1) ** (1/3))


def hIndex(citations):
    if len(citations) == 1:
        return 0 if citations[0] == 0 else 1
    shell_sort(citations)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return i
        if i + 1 == len(citations):
            return i + 1


list = [11, 15]
print(hIndex(list))
