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
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_path = 0

        def _max_path(node, last_val):
            nonlocal max_path

            if not node or node.val is None:
                return 0

            left_max, right_max = _max_path(node.left, node.val), _max_path(node.right, node.val)
            max_p = max(left_max, right_max) + 1
            max_path = max(max_path, max_p)
            if node.val != last_val:
                return 0
            else:
                return max_p

        if root:
            _max_path(root, root.val)
        return max_path


class Solution2:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxL = 0

        def getMaxL(node, val):
            nonlocal maxL
            if not root:
                return 0
            leftMaxL = getMaxL(node.left, node.val)
            rightMaxL = getMaxL(node.right, node.val)

            maxL = max(maxL, leftMaxL + rightMaxL)

            if (node.val == val):
                return max(leftMaxL, rightMaxL) + 1
            else:
                return 0

        if root:
            getMaxL(root, root.val)
        return maxL


if __name__ == '__main__':
    s = Solution2()
    root = Tree('[4, 4, 4, 4, 4, 4, 4]')
    print(s.longestUnivaluePath(root))
