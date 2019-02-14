#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (63.45%)
# Total Accepted:    18.4K
# Total Submissions: 28.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """
    递归解法
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        vals = []
        self._inorderTraversal(root, vals)
        return vals

    def _inorderTraversal(self, root, vals):
        if not root:
            return

        if root.left:
            self._inorderTraversal(root.left, vals)
        
        vals.append(root.val)

        if root.right:
            self._inorderTraversal(root.right, vals)
        
        return

class Solution:
    """
    循环解法
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        vals = []
        inn = [root]

        history = set()
        while inn:
            node = inn.pop(-1)

            if not node:
                continue

            if node.left and node.left not in history:
                inn.append(node)
                inn.append(node.left)
                history.add(node.left)
                continue
            
            vals.append(node.val)

            if node.right and node.right not in history:
                inn.append(node.right)
                history.add(node.right)
                continue
        
        return vals
        
