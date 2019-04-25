#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = []
        next_stack = [root]
        res = []
        index = - 1
        while next_stack:
            stack = next_stack
            next_stack = []
            vals = []
            index = 1 if index == - 1 else - 1
            while stack:
                node = stack.pop(0)
                if node.left:
                    next_stack.append(node.left)

                if node.right:
                    next_stack.append(node.right)

                vals.append(node.val)

            res.append(vals[::index])

        return res
