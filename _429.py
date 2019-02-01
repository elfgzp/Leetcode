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

        next_stack = [root]
        res = []
        tmp_res = [root.val]

        while next_stack:
            stack = deepcopy(next_stack)
            next_stack = []
            res.append(tmp_res)
            tmp_res = []
            while stack:
                first = stack.pop(0)
                for child in first.children:
                    next_stack.append(child)
                    tmp_res.append(child.val)

        return res
