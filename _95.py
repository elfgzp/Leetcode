# -*- coding: utf-8 -*-
__author__ = 'gzp'

from utils import TreeNode


class Solution:
    cache = {}

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self._generateTrees(1, n)

    def _generateTrees(self, left, right):
        if left > right:
            return [None]

        if (left, right) in self.cache.keys():
            return self.cache[(left, right)]

        res = []
        for i in range(left, right + 1):
            left_nodes = self._generateTrees(left, i - 1)
            right_nodes = self._generateTrees(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)

        self.cache[(left, right)] = res
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generateTrees(3)
    for each in res:
        print(each.get_nodes())
