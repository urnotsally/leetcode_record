# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        list = []

        def walk_through_node(a):
            if not a:
                return
            walk_through_node(a.right)
            list.append(a.val)
            walk_through_node(a.left)

        walk_through_node(root)

        return list[k-1]