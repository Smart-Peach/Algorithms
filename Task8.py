def count_split_inversions(arr, start1, end1, start2, end2) -> int:
    res = 0
    lsize = end1 - start1 + 1
    rsize = end2 - start2 + 1
    print(f"sizes: {lsize}, {rsize}")
    i = j = 0
    while i < lsize and j < rsize:
        if arr[start1 + i] > arr[start2 + j]:
            res += 1
        i += 1
        j += 1
    return res


def count_inversions(nums, start, end) -> int:
    print(start, end)
    print(nums[start:end])
    if (end - start) == 0:
        print("!!!")
        return 0
    if start < end:
        middle = len(nums) // 2
        print(f"indexes: {start}, {middle}, {middle + 1}, {end}")
        left = count_inversions(nums, start, middle)
        right = count_inversions(nums, middle + 1, end)

        split = count_split_inversions(nums, start, middle, middle + 1, end)
        print(f"adds: {left}, {right}, {split}")
        return left + right + split


l = [1, 0, 2]
print(f"answer: {count_inversions(l, 0, len(l) - 1)}")
