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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._maxDepth(root)

    def _maxDepth(self, node):
        if not node:
            return 0

        left = self._maxDepth(node.left)
        right = self._maxDepth(node.right)

        return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    root = Tree('[3,9,20,null,null,15,7]')
    print(s.maxDepth(root))
