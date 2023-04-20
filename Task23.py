# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check_right(head, top):
            if head.right:
                return (head.val < head.right.val) and head.right.val < top
            return True

        def check_left(head, bottom):
            if head.left:
                return (head.val > head.left.val) and head.left.val > bottom
            return True

        def is_BST(root, bottom, top, f):

            if not (check_right(root, top) and check_left(root, bottom)):
                return False

            if root.left:
                top1 = root.val
                f = is_BST(root.left, bottom, top1, f)
            if root.right and f:
                bottom1 = root.val
                f = is_BST(root.right, bottom1, top, f)
            if f:
                return True

        return is_BST(root, -2 ** 31 - 1, 2 ** 31, True)
