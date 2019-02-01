# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import Tree


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        self._inorderTraversal(root, vals)
        return vals

    def _inorderTraversal(self, node, vals):
        if not node:
            return

        if node.left:
            self._inorderTraversal(node.left, vals)

        vals.append(node.val)

        if node.right:
            self._inorderTraversal(node.right, vals)

        return


if __name__ == '__main__':
    s = Solution()
    print( Tree('[1,null,2,3]').get_nodes())
    print(s.inorderTraversal(Tree('[1,null,2,3]')))
