# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        
        def postorder(node):
            if not node:
                return -1
            leftH = postorder(node.left)
            rightH = postorder(node.right)
            self.dia = max(self.dia, leftH + rightH + 2)
            
            return 1 + max(leftH, rightH)
        
        postorder(root)
        return self.dia
        