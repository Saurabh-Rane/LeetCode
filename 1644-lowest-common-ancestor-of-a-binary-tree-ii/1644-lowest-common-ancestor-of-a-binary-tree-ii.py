# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.checkp, self.checkq = False, False
        def postorder(node):
            if not node:
                return None
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            if node == p:
                self.checkp = True
                return node
            elif node == q:
                self.checkq = True
                return node
            
            if left and right:
                return node
            
            return left if left else right
        
        ans = postorder(root)
        return ans if (self.checkp and self.checkq) else None
            
        
        