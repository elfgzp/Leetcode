# -*- coding: utf-8 -*-
__author__ = 'gzp'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import Tree


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        return self._trimBST(root, L, R)

    def _trimBST(self, node, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if not node:
            return

        if node.val is not None and node.val < L:
            node = self._trimBST(node.right, L, R)

        elif node.val is not None and node.val > R:
            node = self._trimBST(node.left, L, R)

        if not node:
            return

        node.right = self._trimBST(node.right, L, R)
        node.left = self.trimBST(node.left, L, R)
        return node


if __name__ == '__main__':
    s = Solution()
    root = Tree([1, 0, 2])
    print(root.get_nodes())
    print(s.trimBST(root, 1, 2).get_nodes())

    root = Tree([3, 0, 4, None, 2, None, None, 1])
    print(root.get_nodes())
    print(s.trimBST(root, 1, 3).get_nodes())
