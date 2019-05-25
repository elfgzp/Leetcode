"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        nodes = []
        self._pre_order(root, nodes)
        
        length = len(nodes)
        
        for i in range(1, length):
            nodes[i - 1].right,  nodes[i].left = nodes[i], nodes[i - 1]
        
        nodes[0].left, nodes[-1].right = nodes[-1], nodes[0]
        
        return nodes[0]
    
    def _pre_order(self, root: 'Node', nodes: list) -> list:
        if not root:
            return
        
        if root.left:
            self._pre_order(root.left, nodes)
        
        nodes.append(root)
        
        if root.right:
            self._pre_order(root.right, nodes)

