# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)
        while root:
            if root.val > maximum:
                root = root.left
            elif root.val < minimum:
                root = root.right
            else:
                return root
        return None

