# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        
        def helper(node, path, sum):
            sum += node.val
            path = path + [node.val]
            
            if node.left:
                helper(node.left, path, sum)
            if node.right:
                helper(node.right, path, sum)
            if not node.left and not node.right and sum == targetSum:
                self.res.append(path)
        if not root:
            return []
        helper(root, [], 0)
        return self.res