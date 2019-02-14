# -*- coding: utf-8 -*-
__author__ = 'gzp'

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from copy import deepcopy


class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        next_inn = [root]
        res = []
        tmp_res = [root.val]

        while next_inn:
            inn = deepcopy(next_inn)
            next_inn = []
            res.append(tmp_res)
            tmp_res = []
            while inn:
                first = inn.pop(0)
                for child in first.children:
                    next_inn.append(child)
                    tmp_res.append(child.val)

        return res
