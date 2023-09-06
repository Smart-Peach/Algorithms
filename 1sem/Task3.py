def search(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        middle = l + (r - l) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            l = middle + 1
        else:
            r = middle
    return -1


print(search([5], 5))
