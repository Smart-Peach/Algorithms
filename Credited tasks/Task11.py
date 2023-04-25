def swap(array, ind1, ind2):
    const = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = const


def sort_colors(nums):
    i = k = 0
    j = len(nums) - 1
    while k <= j:
        if nums[k] == 0:
            swap(nums, i, k)
            i += 1
            k += 1
        elif nums[k] == 2:
            swap(nums, j, k)
            j -= 1
        else:
            k += 1


# arr = [2, 0, 2, 1, 1, 0]
# arr = [2, 0, 1]
arr = [1, 2, 0]
sort_colors(arr)
print(arr)
