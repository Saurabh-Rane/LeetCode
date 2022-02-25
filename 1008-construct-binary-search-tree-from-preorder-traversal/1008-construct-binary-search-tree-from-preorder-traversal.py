# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def helper(left, right):
            nonlocal index, n
            if index == n:
                return None
            
            currVal = preorder[index]
            if currVal < left or currVal > right:
                return None
            index += 1
            curr = TreeNode(currVal)
            curr.left = helper(left, currVal)
            curr.right = helper(currVal ,right)
            
            
            return curr

        index = 0
        return helper(-sys.maxsize, sys.maxsize)