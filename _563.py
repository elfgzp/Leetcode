# -*- coding: utf-8 -*-
__author__ = 'gzp'

from utils import Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        _, tilt = self._findTilt(root)
        return tilt

    def _findTilt(self, node):
        if not node:
            return 0, 0

        left_val, left_tilt = self._findTilt(node.left)
        right_val, right_tilt = self._findTilt(node.right)
        return node.val + left_val + right_val, abs(left_val - right_val) + left_tilt + right_tilt



class Solution2(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find(root):
            if not root:
                return 0, 0

            ldif, lsm = find(root.left)
            rdif, rsm = find(root.right)

            return abs(lsm - rsm) + ldif + rdif, lsm + rsm + root.val

        d, s = find(root)

        return d


if __name__ == '__main__':
    s = Solution()
    root = Tree([1, 2, 3])
    print((s.findTilt(root)))
