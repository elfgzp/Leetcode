# -*- coding: utf-8 -*-
__author__ = 'gzp'

from utils import Tree


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self._tree_leaves(root1) == self._tree_leaves(root2)

    def _tree_leaves(self, node, leaves=None):
        if not node:
            return leaves

        if leaves is None:
            leaves = []

        if node.left:
            self._tree_leaves(node.left, leaves=leaves)

        if node.right:
            self._tree_leaves(node.right, leaves=leaves)

        if not node.left and not node.right:
            leaves.append(node.val)
            return leaves

        return leaves


if __name__ == '__main__':
    s = Solution()

    # r1 = Tree('[3,5,1,6,2,9,8,null,null,7,4]')
    # r2 = Tree('[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    # print(s.leafSimilar(r1, r2))
    #
    # r3 = Tree('[1]')
    # r4 = Tree('[2]')
    # print(r3.get_nodes())
    # print(r4.get_nodes())
    #
    # print(s.leafSimilar(r3, r4))

    r5 = Tree('[1,2,3]')
    r6 = Tree('[1,3,2]')
    print(r5.get_nodes())
    print(r6.get_nodes())

    print(s._tree_leaves(r5))
    print(s._tree_leaves(r6))
    print(s.leafSimilar(r5, r6))
