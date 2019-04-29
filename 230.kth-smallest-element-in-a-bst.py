#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        self._sub_preorder(root, k, nums)
        return nums[-1]

    def _sub_preorder(self, root, k, nums):
        if root.left:
            self._sub_preorder(root.left, k, nums)

        if len(nums) >= k:
            return

        nums.append(root.val)

        if root.right:
            self._sub_preorder(root.right, k, nums)
