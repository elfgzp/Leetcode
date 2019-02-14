# -*- coding: utf-8 -*-
__author__ = 'gzp'

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        if not root.children:
            return 1

        return max(map(lambda n: self.maxDepth(n), root.children)) + 1


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        inn = root.children
        depth = 1
        while inn:
            depth += 1
            tmp = []
            for node in inn:
                if node.children:
                    tmp += node.children

            inn = tmp

        return depth







