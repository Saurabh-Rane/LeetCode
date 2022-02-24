# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            nonlocal index, n
            
            if index == n:
                return None
            
            currval = preorder[index]
            if currval < left or currval > right:
                return None
            curr = TreeNode(currval)
            index += 1
            curr.left = helper(left, currval)
            curr.right = helper(currval, right)
            return curr
        index = 0
        n = len(preorder)
        return helper(-sys.maxsize, sys.maxsize)
        