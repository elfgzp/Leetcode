# -*- coding: utf-8 -*-
__author__ = 'gzp'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        if not root:
            return []

        if not root.left and not root.right:
            res.append(str(root.val))
            return res

        left = self.binaryTreePaths(root.left)
        for each in left:
            res.append(str(root.val) + '->' + each)

        right = self.binaryTreePaths(root.right)
        for each in right:
            res.append(str(root.val) + '->' + each)

        return res




