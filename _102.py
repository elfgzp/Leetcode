# -*- coding: utf-8 -*-
__author__ = 'gzp'

from utils import Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from copy import deepcopy


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
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
                if first.left and first.left.val is not None:
                    next_stack.append(first.left)
                    tmp_res.append(first.left.val)

                if first.right and first.right.val is not None:
                    next_stack.append(first.right)
                    tmp_res.append(first.right.val)

        return res


if __name__ == '__main__':
    s = Solution()
    root = Tree([3, 9, 20, None, None, 15, 7])
    print(root.get_nodes())
    print(s.levelOrder(root))

    root = Tree('[-8,3,0,-8,null,null,null,null,-1,null,8]')
    print(root.get_nodes())
    print(s.levelOrder(root))
