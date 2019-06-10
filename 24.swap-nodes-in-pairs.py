# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        return self._swapPairs(head, head.next)

    def _swapPairs(self, node, node_next):
        
        if node_next and node_next.next:
            node_next.next, node.next = node, self._swapPairs(node_next.next, node_next.next.next)
        elif node_next:
            node_next.next, node.next = node, node_next.next
        else:
            return node
        
        return node_next

