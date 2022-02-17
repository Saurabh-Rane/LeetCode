# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        hashset = set()
        for i in nodes:
            hashset.add(i)
            
        def postorder(node):
            if not node:
                return None
            
            if node in hashset:
                return node
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            if left and right:
                return node
            
            if left and not right:
                return left
            
            if not left and right:
                return right
            
            return None
        
        return postorder(root)