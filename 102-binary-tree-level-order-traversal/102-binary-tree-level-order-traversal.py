# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                res.append(level)
        
        return res
                