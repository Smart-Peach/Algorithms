# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        prestart = start = end = None
        node = head
        for i in range(1, left + 1):
            if i == left - 1:
                prestart = node
            if i == left:
                start = node
            node = node.next

        pred = None
        curr = start

        # Reversion
        for i in range(right - left + 1):
            xt = curr.next
            curr.next = pred
            pred = curr
            curr = xt

        start.next = curr
        end = pred

        if prestart:
            prestart.next = pred
            return head
        return end

