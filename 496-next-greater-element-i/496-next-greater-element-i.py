class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        
        for i in nums2:
            while stack and i > stack[-1]:
                hashmap[stack.pop()] = i
            stack.append(i)
        
        while stack:
            hashmap[stack.pop()] = -1
            
            
        for i in nums1:
            stack.append(hashmap[i])
            
        return stack
        