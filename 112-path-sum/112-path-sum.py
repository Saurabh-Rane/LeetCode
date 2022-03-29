# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        def helper(node, currsum):
            currsum += node.val
            
            if node.left:
                helper(node.left, currsum)
            if node.right:
                helper(node.right, currsum)
            if not node.left and not node.right and currsum == targetSum:
                self.ans = True
        if not root:
            return self.ans
        helper(root, 0)
        return self.ans
        