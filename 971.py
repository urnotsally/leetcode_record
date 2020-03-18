# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """

        stack = []
        now = 0
        ans = []

        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            if node.val != voyage[now]:
                return [-1]
            if node.left and node.right:
                if voyage[now+1] == node.left.val:
                    stack.append(node.right)
                    stack.append(node.left)
                elif voyage[now+1] == node.right.val:
                    ans.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    return [-1]
            elif node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)

            now += 1
            if now >= len(voyage)-1:
                return ans
        return ans

