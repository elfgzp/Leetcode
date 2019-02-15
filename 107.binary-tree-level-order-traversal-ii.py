#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (58.09%)
# Total Accepted:    9.1K
# Total Submissions: 15.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其自底向上的层次遍历为：
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from copy import deepcopy

        inn = []
        next_inn = [root]
        res = []

        while inn or next_inn:
            inn = deepcopy(next_inn)
            next_inn = []
            vals = [] 
            while inn:
                node = inn.pop(0)
                if not node:
                    return vals
                
                vals.append(node.val)
                if node.left:
                    next_inn.append(node.left)
                
                if node.right:
                    next_inn.append(node.right)
            res.append(vals)
        
        return res[::-1]

            

