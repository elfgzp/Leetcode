# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        return self.to_bst(nums)
        
    def to_bst(self, nums):
        if not nums:
            return None
        
        length = len(nums)
        
        if length == 1:
            return TreeNode(nums[0])
        
        mid = length // 2
        
        root = TreeNode(nums[mid])
        root.left = self.to_bst(nums[:mid])
        root.right = self.to_bst(nums[mid + 1:])
        
        return root

