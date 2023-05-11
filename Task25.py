# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def calculate_hight(root):
            if not root:
                return -1
            return max(calculate_hight(root.left), calculate_hight(root.right)) + 1

        def balance(root):
            return calculate_hight(root.left) - calculate_hight(root.right)

        def left_rotation(root):
            x = root.right
            root.right = x.left
            x.left = get_rotation(root)
            return get_rotation(x)

        def right_rotation(root):
            x = root.left
            root.left = x.right
            x.right = get_rotation(root)
            return get_rotation(x)

        def get_rotation(root):
            bal = balance(root)
            if bal >= 2:
                if balance(root.left) >= 1:
                    return right_rotation(root)
                else:
                    root.left = left_rotation(root.left)
                    return right_rotation(root)

            elif bal <= -2:
                if balance(root.right) <= -1:
                    return left_rotation(root)
                else:
                    root.right = right_rotation(root.right)
                    return left_rotation(root)

            return root

        if not root:
            return None
        root.left = self.balanceBST(root.left)
        root.right = self.balanceBST(root.right)

        return get_rotation(root)