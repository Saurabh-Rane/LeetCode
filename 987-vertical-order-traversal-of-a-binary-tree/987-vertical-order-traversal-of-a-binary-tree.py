# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = collections.defaultdict(list)
        
        def dfs(x, y, node):
            if not node:
                return
            
            dfs(x - 1, y + 1, node.left)
            dfs(x + 1, y + 1, node.right)
            hashmap[(x, y)].append(node.val)
            
        dfs(0, 0, root)
        res = []
        prev = float('-inf')
        for cord, vals in sorted(hashmap.items()):
            if cord[0] != prev:
                res.append([])
            res[-1].extend(sorted(vals))
            prev = cord[0]
            
        return res
            