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

        result = []
        if root:
            result.append(root.val)
            flag = 1
            Q = [root]
            while Q:
                u = Q[0]
                Q.pop(0)
                if u.left:
                    result.append(u.left.val)
                    Q.append(u.left)
                else:
                    result.append(None)
                if u.right:
                    result.append(u.right.val)
                    Q.append(u.right)
                else:
                    result.append(None)

            while not result[-1]:  # delete
                result.pop(-1)

        string = str(result)
        print(string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(', ')
        print(data)
        head = TreeNode()
        if len(data):
            Q = [head]
            head.val = data[0]
            i = 0
            while Q:
                print(Q)
                u = Q[0]
                Q.pop(0)
                # print(u.val)
                # u.left = TreeNode()
                # u.right = TreeNode()
                if 2 * i + 1 < len(data) and u.val != 'None':
                    print(u.val)
                    u.left = TreeNode()
                    u.left.val = data[2 * i + 1] if data[2 * i + 1] != 'null' else None
                    Q.append(u.left)
                if 2 * i + 2 < len(data) and u.val != 'None':
                    print(u.val)
                    u.right = TreeNode()
                    u.right.val = data[2 * i + 2] if data[2 * i + 2] != 'null' else None
                    Q.append(u.right)
                i += 1

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))