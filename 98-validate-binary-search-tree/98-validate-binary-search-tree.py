# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, left, right):
            if not node:
                return True
            elif not (node.val < right and node.val > left):
                return False
            
            return validateBST(node.left, left, node.val) and validateBST(node.right, node.val, right)
        
        return validateBST(root, float('-inf'), float('inf'))
        