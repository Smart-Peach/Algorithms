def reverseBetween(self, head, left, right):
    prestart = start = end = None
    node = head
    for i in range(1, right + 1):
        if i == left - 1:
            prestart = node
        if i == left:
            start = node
        if i == right:
            end = node
        node = node.next
    act_end = end.next

    pred = None
    curr = start
    # Reversion
    for i in range(right - left + 1):
        xt = curr.next
        curr.next = pred
        pred = curr
        curr = xt
    start.next = act_end

    if prestart:
        prestart.next = end
        return head
    return end
