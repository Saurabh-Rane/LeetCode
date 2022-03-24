# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
                print(len(lists), i)
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergesort(list1, list2))
            lists = mergedList
        
        return lists[0]
                
    def mergesort(self, list1, list2):
        node = ListNode()
        temp = node
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return node.next