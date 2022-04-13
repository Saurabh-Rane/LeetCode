class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            set1, set2 = set(nums1), set(nums2)
        else:
            set1, set2 = set(nums2), set(nums1)
        res = []
        
        for i in set1:
            if i in set2:
                res.append(i)
        
        return res
                
        
        