#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.42%)
# Total Accepted:    20.5K
# Total Submissions: 45.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if left is None and right is None:
            return True

        if left and right and left.val == right.val:
            return self.is_mirror(left.right, right.left) and self.is_mirror(left.left, right.right)

        return False


class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        inn = [(root.left, root.right)]
        history = set()

        while inn:
            left, right = inn.pop(0)
            if (left, right) in history:
                continue

            if left is None and right is None:
                continue

            if left and right and left.val == right.val:
                inn.append((left.right, right.left))
                inn.append((left.left, right.right))
                history.add((left, right))
                continue

            return False
        else:
            return True


class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self._is_mirror(root.left, root.right)

    def _is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None or right is None:
            return left == right

        return left.val == right.val and self._is_mirror(left.left, right.right) and self._is_mirror(right.left, left.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        inn = []
        next_inn = [(root.left, root.right)]

        while inn or next_inn:
            inn = next_inn
            next_inn = []
            while inn:
                left, right = inn.pop(-1)

                if left is None and right is not None:
                    return False

                if left is not None and right is None:
                    return False

                if left is None and right is None:
                    continue

                if left.val != right.val:
                    return False

                next_inn.extend([(left.left, right.right), (right.left, left.right)])

        return True
