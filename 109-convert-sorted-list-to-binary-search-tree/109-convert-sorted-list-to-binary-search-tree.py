# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        def helper(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = TreeNode(array[mid])
            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)
            return node
        
        return helper(0, len(array) - 1)