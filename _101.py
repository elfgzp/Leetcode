# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import Tree


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)

    def is_mirror(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val == right.val and \
               self.is_mirror(left.right, right.left) \
               and self.is_mirror(left.left, right.right)


if __name__ == '__main__':
    s = Solution()
    root = Tree([1, 2, 2, 3, 4, 4, 3])
    print(root.get_nodes())
    print(s.isSymmetric(root))
