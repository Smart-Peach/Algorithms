import random


class Node:
    def __init__(self, val: int = None, left=None, right=None):
        self.val = val
        self.priority = random.randint(0, 2 ** 32 - 1)
        self.size = 1
        self.sum = val

        self.left = left
        self.right = right


class Treap:
    def __init__(self):
        self.head = None

    def get_size(self, t: Node) -> int:
        if t:
            return t.size
        return 0

    def get_sum(self, t: Node) -> int:
        if t:
            return t.sum
        return 0

    def insert(self, val: int, pos: int) -> None:
        l, r = self.split_by_size(self.head, pos - 1)
        new = Node(val=val)
        t1 = self.merge(l, new)
        t2 = self.merge(t1, r)
        self.head = t2

    def erase(self, t: Node, pos: int) -> None:
        l, r = self.split_by_size(t, pos - 1)
        e, rr = self.split_by_size(r, 1)
        self.head = self.merge(l, rr)

    def summa(self, _from: int, _to: int) -> int:
        l, r = self.split_by_size(self.head, _from - 1)
        rl, rr = self.split_by_size(r, _to - _from + 1)
        return rl.sum

    def get_key(self, key):
        pass

    def split_by_size(self, t: Node, size: int) -> (Node, Node):
        if not t:
            return None, None
        # print(t.val)

        if size <= self.get_size(t.left):
            ll, lr = self.split_by_size(t.left, size)
            t.left = lr
            self.update(t)
            return ll, t
        else:
            rl, rr = self.split_by_size(t.right, size - self.get_size(t.left) - 1)
            t.right = rl
            self.update(t)
            return t, rr

    def update(self, t: Node):
        t.size = 1 + self.get_size(t.left) + self.get_size(t.right)
        t.sum = t.val + self.get_sum(t.left) + self.get_sum(t.right)

    def merge(self, t1: Node, t2: Node) -> Node:
        if not t1:
            return t2
        if not t2:
            return t1

        if t1.priority < t2.priority:
            t1.right = self.merge(t1.right, t2)
            self.update(t1)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            self.update(t2)
            return t2

    def print_bst(self, root: Node):
        if not root:
            return 'x'
        a = '(' + str(root.val) + " " + str(root.size) + ')'
        return a + " " + self.print_bst(root.left) + " " + self.print_bst(root.right)

    def print_numbers(self, root: Node):
        if root.left:
            self.print_numbers(root.left)
        print(root.val, end=' ')
        if root.right:
            self.print_numbers(root.right)


A = Treap()
A.insert(5, 1)
print(A.print_numbers(A.head))
A.insert(17, 2)
print(A.print_numbers(A.head))
A.insert(99, 2)
print(A.print_numbers(A.head))
A.insert(2, 3)
print(A.print_numbers(A.head))
A.insert(24, 2)
print(A.print_numbers(A.head))
A.insert(13, 3)
print(A.print_numbers(A.head))
A.insert(42, 3)
print(A.print_bst(A.head))
print(A.print_numbers(A.head))
print(A.summa(1, 7))
