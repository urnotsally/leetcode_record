# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0

        def addNode(root):
            if not root:
                return
            if root.right:
                addNode(root.right)
            root.val += self.sum
            self.sum = root.val
            if root.left:
                addNode(root.left)

        addNode(root)
        return root
