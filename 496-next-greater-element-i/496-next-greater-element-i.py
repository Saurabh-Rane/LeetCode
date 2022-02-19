class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            found = 0
            for j in nums2[nums2.index(i) + 1 :]:
                if j > i:
                    found = j
                    break
            if found:
                res.append(found)
            else:
                res.append(-1)
        return res
             
        