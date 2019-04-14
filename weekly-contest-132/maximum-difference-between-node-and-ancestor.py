# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        if not root:
            return None
        
        res, _, _ = self._maxAncestorDiff(root)
        return res
    
    def _maxAncestorDiff(self, root: TreeNode):
        if not root.left and not root.right:
            return float('-inf'), root.val, root.val
    
        if not root.left:
            max_res, min_val, max_val = self._maxAncestorDiff(root.right)
        elif not root.right:
            max_res, min_val, max_val = self._maxAncestorDiff(root.left)
        else:
            left_res, left_min, left_max = self._maxAncestorDiff(root.left)
            right_res, right_min, right_max = self._maxAncestorDiff(root.right)
            min_val = min(left_min, right_min)
            max_val = max(left_max, right_max)
            max_res = max(left_res, right_res)
            
        res = max(abs(root.val - min_val), abs(root.val - max_val))
        return max(max_res, res), min(min_val, root.val), max(max_val, root.val)
