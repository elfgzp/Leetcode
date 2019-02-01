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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self._mergeTrees(t1, t2)

    def _mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None

        if not t1:
            return t2

        if not t2:
            return t1

        t1.val = (t1.val or 0) + (t2.val or 0)
        t1.left = self._mergeTrees(t1.left, t2.left)
        t1.right = self._mergeTrees(t1.right, t2.right)

        return t1


if __name__ == '__main__':
    s = Solution()
    t1 = Tree('[1,3,2,5]')
    t2 = Tree('[2,1,3,null,4,null,7]')
    t = s.mergeTrees(t1, t2)
    print(t.get_nodes())

