# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def view(root, counter, max, result):
            if root:
                counter += 1
                if counter > max:
                    result.append(root.val)
                    max = counter
                if root.right:
                    result, max = view(root.right, counter, max, result)
                if root.left:
                    result, max = view(root.left, counter, max, result)
            return result, max

        return (view(root, 0, -101, [])[0])
