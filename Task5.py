def hIndex(citations):
    arr = sorted(citations, reverse=True)
    for i in range(len(arr)):
        if i + 1 > arr[i]:
            return i


list = [1, 3, 1]
print(hIndex(list))
