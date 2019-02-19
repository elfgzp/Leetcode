#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (48.04%)
# Total Accepted:    4.3K
# Total Submissions: 8.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

