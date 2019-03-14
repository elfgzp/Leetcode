#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (23.89%)
# Total Accepted:    13.8K
# Total Submissions: 57.7K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root)

    def _isValidBST(self, root, min_node=None, max_node=None):
        if not root:
            return True

        if min_node and min_node.val >= root.val:
            return False

        if max_node and max_node.val <= root.val:
            return False

        return self._isValidBST(root.left, min_node, root) and self._isValidBST(root.right, root, max_node)


class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        last = None
        cur = None
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

            last, cur = cur, node.val

            if last is not None and cur is not None and last >= cur:
                return False

            if node.right and node.right not in history:
                inn.append(node.right)
                history.add(node.right)
                continue

        return True


class Solution3(object):
    def isValidBST(self, root):
        inorder = self._inorder(root)
        return inorder == sorted(set(inorder), key=lambda x: x)

    def _inorder(self, root):
        inorder = []
        history = set()
        inn = []

        while root:
            while root.left and root.left not in history:
                inn.append(root)
                root = root.left

            inorder.append(root.val)
            history.add(root)

            if root.right and root.right not in history:
                root = root.right
            elif inn:
                root = inn.pop(-1)
            else:
                root = None

        return inorder


class Solution(object):
    def isValidBST(self, root):
        return self._isValidBST(root, None, None)

    def _isValidBST(self, root, min_val, max_val):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if min_val is not None and root.val <= min_val:
            return False

        if max_val is not None and root.val >= max_val:
            return False

        if not root.left and not root.right:
            return True

        if not root.left:
            return self._isValidBST(root.right, root.val, max_val)

        if not root.right:
            return self._isValidBST(root.left, min_val, root.val)

        return self._isValidBST(root.right, root.val, max_val) and self._isValidBST(root.left, min_val, root.val)
