# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serializeDFS(self, node, values):
        if not node:
            values.append("#")
            return

        values.append(str(node.val))

        self.serializeDFS(node.left, values)
        self.serializeDFS(node.right, values)

    def serialize(self, root):
        values = []

        self.serializeDFS(root, values)

        return ",".join(values)

    def deserializeDFS(self, values):
        value = values[self.index]
        self.index += 1

        if value == "#":
            return None

        root = TreeNode(int(value))

        root.left = self.deserializeDFS(values)
        root.right = self.deserializeDFS(values)

        return root

    def deserialize(self, data):
        values = data.split(",")

        self.index = 0

        return self.deserializeDFS(values)