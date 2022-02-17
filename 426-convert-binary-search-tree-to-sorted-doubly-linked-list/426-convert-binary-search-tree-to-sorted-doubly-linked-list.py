"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.head = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if not self.head:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev
                
            self.prev = node
            
            inorder(node.right)
            
        
        inorder(root)
        if not root:
            return None
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head