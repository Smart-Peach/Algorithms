# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return 'x'
        return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def pre_deser(data):
            if len(data):
                head = TreeNode()

                if data[0] != 'x':
                    head.val = data[0]
                else:
                    head = None

                data.pop(0)
                if head:
                    head.left = pre_deser(data)
                    head.right = pre_deser(data)
                return head

        nodes = []
        if len(data) != 1:
            nodes = data.split()

        return pre_deser(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))