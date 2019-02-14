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
                if first.left and first.left.val is not None:
                    next_inn.append(first.left)
                    tmp_res.append(first.left.val)

                if first.right and first.right.val is not None:
                    next_inn.append(first.right)
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
