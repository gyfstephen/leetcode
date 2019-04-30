# coding=utf-8
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


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
        if root.val > p.val and root.val > q.val:
            self.lowestCommonAncestor(root.right, p, q)
        elif root.val < p.val and root.val < q.val:
            self.lowestCommonAncestor(root.left, p, q)
        else:
            return root