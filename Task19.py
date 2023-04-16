# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def swap(array, pos1, pos2):
    const = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = const


def sift_up(array):
    value = array[-1].val
    i = len(array) - 1
    while i:
        if array[(i - 1) // 2].val > value:
            const = array[i]
            array[i] = array[(i - 1) // 2]
            array[(i - 1) // 2] = const
            i = (i - 1) // 2
        else:
            break


def sift_down(array):
    if len(array):
        value = array[0].val
        i = 0
        while 2 * i + 1 < len(array):  # Continue while having children
            if 2 * i + 2 >= len(array):  # If only one child has been stayed
                if array[i * 2 + 1].val < value:
                    swap(array, 2 * i + 1, i)
                break
            elif array[2 * i + 1].val < value or array[i * 2 + 2].val < value:
                if array[2 * i + 1].val < array[2 * i + 2].val:
                    swap(array, 2 * i + 1, i)
                    i = 2 * i + 1
                else:
                    swap(array, 2 * i + 2, i)
                    i = 2 * i + 2
            else:
                break


def merge_k_lists(lists):
    if not len(lists):
        return None

    pyramid = []
    # Create first pyramid
    for i in range(len(lists)):
        if lists[i]:
            pyramid.append(lists[i])
            sift_up(pyramid)

    if not len(pyramid):
        return None

    main_head = pyramid[0]
    head = main_head
    while len(pyramid):
        if pyramid[0].next:
            pyramid[0] = pyramid[0].next
        else:
            swap(pyramid, 0, -1)
            pyramid.pop(-1)
        if len(pyramid):
            sift_down(pyramid)
            head.next = pyramid[0]
            head = head.next

    return main_head
