# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import Tree


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self._isBalanced(root) is False:
            return False

        else:
            return True

    def _isBalanced(self, node):
        if not node:
            return 0

        left = self._isBalanced(node.left)
        right = self._isBalanced(node.right)

        if left is False or right is False:
            return False

        if abs(left - right) > 1:
            return False

        else:
            return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    root = Tree('[3,9,20,null,null,15,7]')
    print(s.isBalanced(root))
