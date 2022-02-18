"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hashset = set()
        
        while p:
            hashset.add(p)
            p = p.parent
            
        while q:
            if q in hashset:
                return q
            q = q.parent
            
        return None