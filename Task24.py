# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        if not root:
            return None

        while root:  # Find new root (if head also should be deleted)
            if root.val < low:  # It should be bigger then go right (bang on the left branch, because it contains only bad numbers)
                root = root.right
            elif root.val > high:  # It should be smaller then go left (bang on the right branch, because it contains only bad numbers)
                root = root.left
            else:
                break

        node = root  # Root is good
        while node:
            while node.left and node.left.val < low:
                node.left = node.left.right
            node = node.left

        node = root
        while node:
            while node.right and node.right.val > high:
                node.right = node.right.left
            node = node.right

        return root
