class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        minval = 0
        
        for i in nums:
            total += i
            minval = min(minval, total)
            
        return -minval + 1