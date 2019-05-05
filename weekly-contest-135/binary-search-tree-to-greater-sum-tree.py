# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._bstToGst(root)
        return root

    def _bstToGst(self, root, val=0):
        if not root.left and not root.right:
            val = root.val + val
            root.val = val
            return val

        if root.right:
            val = root.val + self._bstToGst(root.right, val)
            root.val = val

        if root.left:
            val = self._bstToGst(root.left, root.val)

        return val



