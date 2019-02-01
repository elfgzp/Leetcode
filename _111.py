# -*- coding: utf-8 -*-
__author__ = 'gzp'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import Tree


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)

    def getDepth(self, root):
        if root is None:
            return 0

        if root.right is None:
            return self.getDepth(root.left) + 1

        if root.left is None:
            return self.getDepth(root.right) + 1

        l_height = self.getDepth(root.left) + 1
        r_height = self.getDepth(root.right) + 1

        return min(l_height, r_height)


if __name__ == '__main__':
    s = Solution()
    root = Tree('[3,9,20,null,null,15,7]')
    print(s.minDepth(root))
