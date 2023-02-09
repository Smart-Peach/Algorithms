def search(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        middle = l + (r - l) // 2
        if nums[middle] > target:
            r = middle
        elif nums[middle] < target:
            l = middle + 1
        else:
            return middle
    return -1


print(search([-1, 0, 3, 5, 9, 12], 0))
